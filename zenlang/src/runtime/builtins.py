"""ZenLang Built-in Functions"""
import builtins as py_builtins

# ============ Type Conversion ============

def str(value):
    """Convert value to string"""
    return py_builtins.str(value)

def int(value):
    """Convert value to integer"""
    try:
        return py_builtins.int(value)
    except ValueError:
        return 0

def float(value):
    """Convert value to float"""
    try:
        return py_builtins.float(value)
    except ValueError:
        return 0.0

def bool(value):
    """Convert value to boolean"""
    return py_builtins.bool(value)

# ============ Type Checking ============

def type(value):
    """Get type of value"""
    t = py_builtins.type(value).__name__
    if t == 'list':
        return 'array'
    elif t == 'dict':
        return 'object'
    elif t == 'NoneType':
        return 'null'
    return t

def isNumber(value):
    """Check if value is a number"""
    return py_builtins.isinstance(value, (py_builtins.int, py_builtins.float)) and not py_builtins.isinstance(value, py_builtins.bool)

def isString(value):
    """Check if value is a string"""
    return py_builtins.isinstance(value, py_builtins.str)

def isArray(value):
    """Check if value is an array"""
    return py_builtins.isinstance(value, py_builtins.list)

def isObject(value):
    """Check if value is an object"""
    return py_builtins.isinstance(value, py_builtins.dict)

def isBool(value):
    """Check if value is a boolean"""
    return py_builtins.isinstance(value, py_builtins.bool)

def isNull(value):
    """Check if value is null"""
    return value is None

# ============ Array Functions ============

def length(arr):
    """Get length of array or string"""
    return py_builtins.len(arr)

def push(arr, value):
    """Add element to end of array"""
    if py_builtins.isinstance(arr, py_builtins.list):
        arr.append(value)
        return arr
    return arr

def pop(arr):
    """Remove and return last element"""
    if py_builtins.isinstance(arr, py_builtins.list) and py_builtins.len(arr) > 0:
        return arr.pop()
    return None

def shift(arr):
    """Remove and return first element"""
    if py_builtins.isinstance(arr, py_builtins.list) and py_builtins.len(arr) > 0:
        return arr.pop(0)
    return None

def unshift(arr, value):
    """Add element to beginning of array"""
    if py_builtins.isinstance(arr, py_builtins.list):
        arr.insert(0, value)
        return arr
    return arr

def slice(arr, start, end=None):
    """Get slice of array"""
    if end is None:
        return arr[py_builtins.int(start):]
    return arr[py_builtins.int(start):py_builtins.int(end)]

def indexOf(arr, value):
    """Find index of value in array"""
    try:
        return arr.index(value)
    except ValueError:
        return -1

def includes(arr, value):
    """Check if array includes value"""
    return value in arr

def reverse(arr):
    """Reverse array"""
    if py_builtins.isinstance(arr, py_builtins.list):
        return py_builtins.list(py_builtins.reversed(arr))
    return arr

def sort(arr):
    """Sort array"""
    if py_builtins.isinstance(arr, py_builtins.list):
        return py_builtins.sorted(arr)
    return arr

def join(arr, separator=""):
    """Join array elements into string"""
    if py_builtins.isinstance(arr, py_builtins.list):
        return separator.join(py_builtins.str(x) for x in arr)
    return py_builtins.str(arr)

def filter(arr, func):
    """Filter array elements"""
    if py_builtins.isinstance(arr, py_builtins.list):
        return [x for x in arr if func(x)]
    return arr

def map(arr, func):
    """Map function over array"""
    if py_builtins.isinstance(arr, py_builtins.list):
        return [func(x) for x in arr]
    return arr

# ============ String Functions ============

def upper(text):
    """Convert string to uppercase"""
    return py_builtins.str(text).upper()

def lower(text):
    """Convert string to lowercase"""
    return py_builtins.str(text).lower()

def trim(text):
    """Remove whitespace from both ends"""
    return py_builtins.str(text).strip()

def split(text, separator=" "):
    """Split string into array"""
    return py_builtins.str(text).split(separator)

def replace(text, old, new):
    """Replace occurrences in string"""
    return py_builtins.str(text).replace(old, new)

def startsWith(text, prefix):
    """Check if string starts with prefix"""
    return py_builtins.str(text).startswith(prefix)

def endsWith(text, suffix):
    """Check if string ends with suffix"""
    return py_builtins.str(text).endswith(suffix)

def substring(text, start, end=None):
    """Get substring"""
    if end is None:
        return py_builtins.str(text)[py_builtins.int(start):]
    return py_builtins.str(text)[py_builtins.int(start):py_builtins.int(end)]

def charAt(text, index):
    """Get character at index"""
    try:
        return py_builtins.str(text)[py_builtins.int(index)]
    except IndexError:
        return ""

def repeat(text, count):
    """Repeat string n times"""
    return py_builtins.str(text) * py_builtins.int(count)

# ============ Math Functions (Additional) ============

def sum(arr):
    """Sum of array elements"""
    if py_builtins.isinstance(arr, py_builtins.list):
        return py_builtins.sum(arr)
    return arr

def avg(arr):
    """Average of array elements"""
    if py_builtins.isinstance(arr, py_builtins.list) and py_builtins.len(arr) > 0:
        return py_builtins.sum(arr) / py_builtins.len(arr)
    return 0

def min(arr):
    """Minimum value in array"""
    if py_builtins.isinstance(arr, py_builtins.list) and py_builtins.len(arr) > 0:
        return py_builtins.min(arr)
    return None

def max(arr):
    """Maximum value in array"""
    if py_builtins.isinstance(arr, py_builtins.list) and py_builtins.len(arr) > 0:
        return py_builtins.max(arr)
    return None

# ============ Object Functions ============

def keys(obj):
    """Get object keys"""
    if py_builtins.isinstance(obj, py_builtins.dict):
        return py_builtins.list(obj.keys())
    return []

def values(obj):
    """Get object values"""
    if py_builtins.isinstance(obj, py_builtins.dict):
        return py_builtins.list(obj.values())
    return []

def hasKey(obj, key):
    """Check if object has key"""
    if py_builtins.isinstance(obj, py_builtins.dict):
        return key in obj
    return False

# ============ Utility Functions ============

def range(start, end=None, step=1):
    """Create array of numbers"""
    if end is None:
        return py_builtins.list(py_builtins.range(py_builtins.int(start)))
    return py_builtins.list(py_builtins.range(py_builtins.int(start), py_builtins.int(end), py_builtins.int(step)))

def print(*args):
    """Print values (alias for zenout.console)"""
    py_builtins.print(*args)

def input(prompt=""):
    """Get user input (alias for zenin.console)"""
    return py_builtins.input(prompt)


# ============ Advanced Array Functions ============

def flatten(arr, depth=None):
    """Flatten nested arrays"""
    result = []
    
    def flatten_helper(items, current_depth):
        for item in items:
            if py_builtins.isinstance(item, py_builtins.list) and (depth is None or current_depth < depth):
                flatten_helper(item, current_depth + 1)
            else:
                result.append(item)
    
    flatten_helper(arr, 0)
    return result

def chunk(arr, size):
    """Split array into chunks"""
    return [arr[i:i + size] for i in py_builtins.range(0, py_builtins.len(arr), size)]

def zip(*arrays):
    """Zip multiple arrays together"""
    return py_builtins.list(py_builtins.zip(*arrays))

def unique(arr):
    """Get unique elements"""
    seen = []
    for item in arr:
        if item not in seen:
            seen.append(item)
    return seen

def compact(arr):
    """Remove falsy values"""
    return [x for x in arr if x]

def difference(arr1, arr2):
    """Elements in arr1 not in arr2"""
    return [x for x in arr1 if x not in arr2]

def intersection(arr1, arr2):
    """Common elements"""
    return [x for x in arr1 if x in arr2]

def union(arr1, arr2):
    """All unique elements from both arrays"""
    return unique(arr1 + arr2)

# ============ Advanced String Functions ============

def capitalize(text):
    """Capitalize first letter"""
    s = py_builtins.str(text)
    return s[0].upper() + s[1:] if s else s

def titleCase(text):
    """Title case all words"""
    return py_builtins.str(text).title()

def reverse(text):
    """Reverse string"""
    return py_builtins.str(text)[::-1]

def count(text, substring):
    """Count occurrences of substring"""
    return py_builtins.str(text).count(substring)

def padStart(text, length, char=" "):
    """Pad string at start"""
    s = py_builtins.str(text)
    return s.rjust(length, char)

def padEnd(text, length, char=" "):
    """Pad string at end"""
    s = py_builtins.str(text)
    return s.ljust(length, char)

def truncate(text, length, suffix="..."):
    """Truncate string"""
    s = py_builtins.str(text)
    if py_builtins.len(s) <= length:
        return s
    return s[:length] + suffix

def slugify(text):
    """Convert to URL-friendly slug"""
    s = py_builtins.str(text).lower()
    s = s.replace(" ", "-")
    return s

def contains(text, substring):
    """Check if string contains substring"""
    return substring in py_builtins.str(text)

# ============ Object/Dict Functions ============

def merge(obj1, obj2):
    """Merge two objects"""
    if py_builtins.isinstance(obj1, py_builtins.dict) and py_builtins.isinstance(obj2, py_builtins.dict):
        result = obj1.copy()
        result.update(obj2)
        return result
    return obj1

def pick(obj, keys_list):
    """Pick specific keys from object"""
    if py_builtins.isinstance(obj, py_builtins.dict):
        return {k: obj[k] for k in keys_list if k in obj}
    return {}

def omit(obj, keys_list):
    """Omit specific keys from object"""
    if py_builtins.isinstance(obj, py_builtins.dict):
        return {k: v for k, v in obj.items() if k not in keys_list}
    return {}

def entries(obj):
    """Get object entries as array of [key, value] pairs"""
    if py_builtins.isinstance(obj, py_builtins.dict):
        return [[k, v] for k, v in obj.items()]
    return []

def fromEntries(entries_list):
    """Create object from entries"""
    return {entry[0]: entry[1] for entry in entries_list if py_builtins.len(entry) >= 2}

# ============ Number Functions ============

def clamp(value, min_val, max_val):
    """Clamp value between min and max"""
    return py_builtins.max(min_val, py_builtins.min(max_val, value))

def lerp(start, end, t):
    """Linear interpolation"""
    return start + (end - start) * t

def random(min_val=0, max_val=1):
    """Random number between min and max"""
    import random as pyrandom
    return pyrandom.uniform(min_val, max_val)

def randomInt(min_val, max_val):
    """Random integer between min and max"""
    import random as pyrandom
    return pyrandom.randint(min_val, max_val)

def round(num, decimals=0):
    """Round to decimal places"""
    return py_builtins.round(num, decimals)

def abs(num):
    """Absolute value"""
    return py_builtins.abs(num)

def sign(num):
    """Sign of number (-1, 0, or 1)"""
    if num > 0:
        return 1
    elif num < 0:
        return -1
    return 0

# ============ Utility Functions ============

def sleep(seconds):
    """Sleep for seconds"""
    import time
    time.sleep(seconds)

def timestamp():
    """Get current timestamp"""
    import time
    return time.time()

def formatNumber(num, decimals=2):
    """Format number with decimals"""
    return py_builtins.format(num, f'.{decimals}f')

def parseJSON(text):
    """Parse JSON string"""
    import json
    try:
        return json.loads(text)
    except:
        return None

def toJSON(obj):
    """Convert object to JSON string"""
    import json
    try:
        return json.dumps(obj)
    except:
        return "{}"

def deepCopy(obj):
    """Deep copy an object"""
    import copy
    return copy.deepcopy(obj)

def isEmpty(value):
    """Check if value is empty"""
    if value is None:
        return True
    if py_builtins.isinstance(value, (py_builtins.str, py_builtins.list, py_builtins.dict)):
        return py_builtins.len(value) == 0
    return False

def isEqual(a, b):
    """Deep equality check"""
    return a == b

def clone(obj):
    """Shallow copy"""
    if py_builtins.isinstance(obj, py_builtins.list):
        return obj.copy()
    elif py_builtins.isinstance(obj, py_builtins.dict):
        return obj.copy()
    return obj


# ============ Advanced Built-in Functions ============

def forEach(arr, func):
    """Execute function for each element"""
    if isinstance(arr, list):
        for item in arr:
            func(item)
    return arr

def reduce(arr, func, initial=None):
    """Reduce array to single value"""
    if not isinstance(arr, list) or len(arr) == 0:
        return initial
    
    if initial is None:
        result = arr[0]
        start = 1
    else:
        result = initial
        start = 0
    
    for i in range(start, len(arr)):
        result = func(result, arr[i])
    
    return result

def every(arr, func):
    """Check if all elements pass test"""
    if isinstance(arr, list):
        return all(func(x) for x in arr)
    return False

def some(arr, func):
    """Check if any element passes test"""
    if isinstance(arr, list):
        return any(func(x) for x in arr)
    return False

def find(arr, func):
    """Find first element matching condition"""
    if isinstance(arr, list):
        for item in arr:
            if func(item):
                return item
    return None

def findIndex(arr, func):
    """Find index of first element matching condition"""
    if isinstance(arr, list):
        for i, item in enumerate(arr):
            if func(item):
                return i
    return -1

def groupBy(arr, key_func):
    """Group array elements by key function"""
    groups = {}
    if py_builtins.isinstance(arr, py_builtins.list):
        for item in arr:
            key = py_builtins.str(key_func(item))  # Convert key to string for consistency
            if key not in groups:
                groups[key] = []
            groups[key].append(item)
    return groups

def sortBy(arr, key_func):
    """Sort array by key function"""
    if py_builtins.isinstance(arr, py_builtins.list):
        return py_builtins.sorted(arr, key=key_func)
    return arr

def take(arr, n):
    """Take first n elements"""
    if isinstance(arr, list):
        return arr[:int(n)]
    return arr

def drop(arr, n):
    """Drop first n elements"""
    if isinstance(arr, list):
        return arr[int(n):]
    return arr

def takeWhile(arr, func):
    """Take elements while condition is true"""
    result = []
    if isinstance(arr, list):
        for item in arr:
            if func(item):
                result.append(item)
            else:
                break
    return result

def dropWhile(arr, func):
    """Drop elements while condition is true"""
    if not isinstance(arr, list):
        return arr
    
    start = 0
    for i, item in enumerate(arr):
        if not func(item):
            start = i
            break
    else:
        return []
    
    return arr[start:]

def partition(arr, func):
    """Partition array into two arrays based on condition"""
    truthy = []
    falsy = []
    if isinstance(arr, list):
        for item in arr:
            if func(item):
                truthy.append(item)
            else:
                falsy.append(item)
    return [truthy, falsy]

def pluck(arr, key):
    """Extract property from array of objects"""
    result = []
    if isinstance(arr, list):
        for item in arr:
            if isinstance(item, dict) and key in item:
                result.append(item[key])
    return result

def countBy(arr, key_func):
    """Count occurrences by key function"""
    counts = {}
    if isinstance(arr, list):
        for item in arr:
            key = key_func(item)
            counts[key] = counts.get(key, 0) + 1
    return counts

def sample(arr, n=1):
    """Get random sample from array"""
    import random
    if py_builtins.isinstance(arr, py_builtins.list) and py_builtins.len(arr) > 0:
        if n == 1:
            return random.choice(arr)
        return random.sample(arr, py_builtins.min(n, py_builtins.len(arr)))
    return None if n == 1 else []

def shuffle(arr):
    """Shuffle array randomly"""
    import random
    if py_builtins.isinstance(arr, py_builtins.list):
        result = arr.copy()
        random.shuffle(result)
        return result
    return arr

def times(n, func):
    """Execute function n times"""
    result = []
    for i in range(int(n)):
        result.append(func(i))
    return result

def debounce(func, delay):
    """Create debounced function"""
    import time
    last_call = [0]
    
    def debounced(*args):
        current = time.time()
        if current - last_call[0] >= delay:
            last_call[0] = current
            return func(*args)
    
    return debounced

def throttle(func, limit):
    """Create throttled function"""
    import time
    last_call = [0]
    
    def throttled(*args):
        current = time.time()
        if current - last_call[0] >= limit:
            last_call[0] = current
            return func(*args)
    
    return throttled

def memoize(func):
    """Memoize function results"""
    cache = {}
    
    def memoized(*args):
        key = str(args)
        if key not in cache:
            cache[key] = func(*args)
        return cache[key]
    
    return memoized

def curry(func, arity=None):
    """Curry a function"""
    if arity is None:
        arity = func.__code__.co_argcount
    
    def curried(*args):
        if len(args) >= arity:
            return func(*args[:arity])
        return lambda *more: curried(*(args + more))
    
    return curried

def compose(*funcs):
    """Compose functions right to left"""
    def composed(x):
        result = x
        for func in reversed(funcs):
            result = func(result)
        return result
    return composed

def pipe(*funcs):
    """Pipe functions left to right"""
    def piped(x):
        result = x
        for func in funcs:
            result = func(result)
        return result
    return piped

def noop():
    """No operation function"""
    pass

def identity(x):
    """Return input unchanged"""
    return x

def constant(value):
    """Return function that always returns value"""
    return lambda: value

def negate(func):
    """Negate function result"""
    return lambda *args: not func(*args)

def once(func):
    """Execute function only once"""
    called = [False]
    result = [None]
    
    def wrapper(*args):
        if not called[0]:
            called[0] = True
            result[0] = func(*args)
        return result[0]
    
    return wrapper
