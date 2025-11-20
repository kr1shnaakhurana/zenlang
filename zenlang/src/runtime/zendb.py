"""ZenLang zendb package - Database and data management library"""
import json
import os
import time
import hashlib

# In-memory database
_databases = {}
_current_db = None

# ============ Database Management ============

class ZenDB:
    """In-memory database with persistence"""
    def __init__(self, name):
        self.name = name
        self.tables = {}
        self.indexes = {}
        self.file_path = f"{name}.zendb"
    
    def create_table(self, table_name, schema=None):
        """Create a new table"""
        if table_name in self.tables:
            raise ValueError(f"Table '{table_name}' already exists")
        
        self.tables[table_name] = {
            'schema': schema or {},
            'data': [],
            'auto_increment': 1
        }
        return True
    
    def insert(self, table_name, record):
        """Insert a record into table"""
        if table_name not in self.tables:
            raise ValueError(f"Table '{table_name}' does not exist")
        
        table = self.tables[table_name]
        
        # Add auto-increment ID if not present
        if 'id' not in record:
            record['id'] = table['auto_increment']
            table['auto_increment'] += 1
        
        # Add timestamp
        record['_created_at'] = time.time()
        
        table['data'].append(record)
        return record['id']
    
    def select(self, table_name, where=None, limit=None):
        """Select records from table"""
        if table_name not in self.tables:
            raise ValueError(f"Table '{table_name}' does not exist")
        
        data = self.tables[table_name]['data']
        
        # Filter by where clause
        if where:
            filtered = []
            for record in data:
                match = True
                for key, value in where.items():
                    if key not in record or record[key] != value:
                        match = False
                        break
                if match:
                    filtered.append(record)
            data = filtered
        
        # Apply limit
        if limit:
            data = data[:limit]
        
        return data
    
    def update(self, table_name, where, updates):
        """Update records in table"""
        if table_name not in self.tables:
            raise ValueError(f"Table '{table_name}' does not exist")
        
        data = self.tables[table_name]['data']
        count = 0
        
        for record in data:
            match = True
            for key, value in where.items():
                if key not in record or record[key] != value:
                    match = False
                    break
            
            if match:
                for key, value in updates.items():
                    record[key] = value
                record['_updated_at'] = time.time()
                count += 1
        
        return count
    
    def delete(self, table_name, where):
        """Delete records from table"""
        if table_name not in self.tables:
            raise ValueError(f"Table '{table_name}' does not exist")
        
        data = self.tables[table_name]['data']
        to_delete = []
        
        for i, record in enumerate(data):
            match = True
            for key, value in where.items():
                if key not in record or record[key] != value:
                    match = False
                    break
            if match:
                to_delete.append(i)
        
        # Delete in reverse order to maintain indices
        for i in reversed(to_delete):
            del data[i]
        
        return len(to_delete)
    
    def count(self, table_name, where=None):
        """Count records in table"""
        return len(self.select(table_name, where))
    
    def save(self):
        """Save database to file"""
        data = {
            'name': self.name,
            'tables': self.tables
        }
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=2)
        return True
    
    def load(self):
        """Load database from file"""
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                self.tables = data.get('tables', {})
            return True
        return False

# ============ Public API ============

def connect(db_name):
    """Connect to or create a database"""
    global _current_db
    
    if db_name not in _databases:
        _databases[db_name] = ZenDB(db_name)
        _databases[db_name].load()  # Try to load from file
    
    _current_db = _databases[db_name]
    return _current_db

def createTable(table_name, schema=None):
    """Create a table in current database"""
    if not _current_db:
        raise ValueError("No database connected")
    return _current_db.create_table(table_name, schema)

def insert(table_name, record):
    """Insert a record"""
    if not _current_db:
        raise ValueError("No database connected")
    return _current_db.insert(table_name, record)

def select(table_name, where=None, limit=None):
    """Select records"""
    if not _current_db:
        raise ValueError("No database connected")
    return _current_db.select(table_name, where, limit)

def update(table_name, where, updates):
    """Update records"""
    if not _current_db:
        raise ValueError("No database connected")
    return _current_db.update(table_name, where, updates)

def delete(table_name, where):
    """Delete records"""
    if not _current_db:
        raise ValueError("No database connected")
    return _current_db.delete(table_name, where)

def count(table_name, where=None):
    """Count records"""
    if not _current_db:
        raise ValueError("No database connected")
    return _current_db.count(table_name, where)

def save():
    """Save current database to file"""
    if not _current_db:
        raise ValueError("No database connected")
    return _current_db.save()

def load():
    """Load current database from file"""
    if not _current_db:
        raise ValueError("No database connected")
    return _current_db.load()

# ============ Query Builder ============

class Query:
    """Query builder for complex queries"""
    def __init__(self, table_name):
        self.table = table_name
        self.where_clause = {}
        self.limit_value = None
        self.order_field = None
        self.order_dir = 'asc'
    
    def where(self, field, value):
        self.where_clause[field] = value
        return self
    
    def limit(self, n):
        self.limit_value = n
        return self
    
    def get(self):
        return select(self.table, self.where_clause, self.limit_value)
    
    def first(self):
        results = self.limit(1).get()
        return results[0] if results else None

def query(table_name):
    """Create a query builder"""
    return Query(table_name)

# ============ Utilities ============

def hash(text):
    """Hash a string (for passwords, etc.)"""
    return hashlib.sha256(str(text).encode()).hexdigest()

def generateId():
    """Generate a unique ID"""
    return hashlib.md5(str(time.time()).encode()).hexdigest()[:16]

def timestamp():
    """Get current timestamp"""
    return time.time()

def now():
    """Get current datetime string"""
    return time.strftime("%Y-%m-%d %H:%M:%S")

# ============ Relationships ============

def hasMany(table, foreign_key, local_id):
    """Get related records (one-to-many)"""
    return select(table, {foreign_key: local_id})

def belongsTo(table, foreign_key, foreign_id):
    """Get parent record (many-to-one)"""
    results = select(table, {'id': foreign_id}, 1)
    return results[0] if results else None

# ============ Aggregations ============

def sum_field(table_name, field, where=None):
    """Sum a field"""
    records = select(table_name, where)
    return sum(r.get(field, 0) for r in records)

def avg_field(table_name, field, where=None):
    """Average a field"""
    records = select(table_name, where)
    if not records:
        return 0
    return sum(r.get(field, 0) for r in records) / len(records)

def max_field(table_name, field, where=None):
    """Maximum value of a field"""
    records = select(table_name, where)
    if not records:
        return None
    return max(r.get(field, 0) for r in records)

def min_field(table_name, field, where=None):
    """Minimum value of a field"""
    records = select(table_name, where)
    if not records:
        return None
    return min(r.get(field, 0) for r in records)

# ============ Migrations ============

def migrate(table_name, add_fields=None, remove_fields=None):
    """Migrate table schema"""
    if not _current_db:
        raise ValueError("No database connected")
    
    if table_name not in _current_db.tables:
        raise ValueError(f"Table '{table_name}' does not exist")
    
    table = _current_db.tables[table_name]
    
    # Add fields
    if add_fields:
        for record in table['data']:
            for field, default in add_fields.items():
                if field not in record:
                    record[field] = default
    
    # Remove fields
    if remove_fields:
        for record in table['data']:
            for field in remove_fields:
                if field in record:
                    del record[field]
    
    return True

# ============ Backup/Restore ============

def backup(filename):
    """Backup current database"""
    if not _current_db:
        raise ValueError("No database connected")
    
    data = {
        'name': _current_db.name,
        'tables': _current_db.tables,
        'backup_time': time.time()
    }
    
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    
    return True

def restore(filename):
    """Restore database from backup"""
    if not _current_db:
        raise ValueError("No database connected")
    
    with open(filename, 'r') as f:
        data = json.load(f)
        _current_db.tables = data.get('tables', {})
    
    return True
