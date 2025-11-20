"""ZenLang fs package - File system operations"""
import os
import json

def read(filepath):
    """Read file content"""
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except Exception as e:
        raise RuntimeError(f"File read error: {e}")

def write(filepath, content):
    """Write content to file"""
    try:
        with open(filepath, 'w') as f:
            f.write(str(content))
        return True
    except Exception as e:
        raise RuntimeError(f"File write error: {e}")

def append(filepath, content):
    """Append content to file"""
    try:
        with open(filepath, 'a') as f:
            f.write(str(content))
        return True
    except Exception as e:
        raise RuntimeError(f"File append error: {e}")

def exists(filepath):
    """Check if file exists"""
    return os.path.exists(filepath)

def delete(filepath):
    """Delete file"""
    try:
        os.remove(filepath)
        return True
    except Exception as e:
        raise RuntimeError(f"File delete error: {e}")

def readJSON(filepath):
    """Read and parse JSON file"""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        raise RuntimeError(f"JSON read error: {e}")

def writeJSON(filepath, data):
    """Write data as JSON to file"""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        raise RuntimeError(f"JSON write error: {e}")

def listdir(path="."):
    """List directory contents"""
    try:
        return os.listdir(path)
    except Exception as e:
        raise RuntimeError(f"Directory list error: {e}")

def mkdir(path):
    """Create directory"""
    try:
        os.makedirs(path, exist_ok=True)
        return True
    except Exception as e:
        raise RuntimeError(f"Directory create error: {e}")


# ============ Advanced File Operations ============

def copy(source, destination):
    """Copy file"""
    try:
        import shutil
        shutil.copy2(source, destination)
        return True
    except Exception as e:
        raise RuntimeError(f"File copy error: {e}")

def move(source, destination):
    """Move/rename file"""
    try:
        import shutil
        shutil.move(source, destination)
        return True
    except Exception as e:
        raise RuntimeError(f"File move error: {e}")

def size(filepath):
    """Get file size in bytes"""
    try:
        return os.path.getsize(filepath)
    except Exception as e:
        raise RuntimeError(f"File size error: {e}")

def extension(filepath):
    """Get file extension"""
    return os.path.splitext(filepath)[1]

def basename(filepath):
    """Get file name without path"""
    return os.path.basename(filepath)

def dirname(filepath):
    """Get directory name"""
    return os.path.dirname(filepath)

def join(*paths):
    """Join path components"""
    return os.path.join(*paths)

def absolute(filepath):
    """Get absolute path"""
    return os.path.abspath(filepath)

def isFile(path):
    """Check if path is a file"""
    return os.path.isfile(path)

def isDir(path):
    """Check if path is a directory"""
    return os.path.isdir(path)

def readLines(filepath):
    """Read file as array of lines"""
    try:
        with open(filepath, 'r') as f:
            return f.readlines()
    except Exception as e:
        raise RuntimeError(f"File read error: {e}")

def writeLines(filepath, lines):
    """Write array of lines to file"""
    try:
        with open(filepath, 'w') as f:
            f.writelines(lines)
        return True
    except Exception as e:
        raise RuntimeError(f"File write error: {e}")

def search(directory, pattern):
    """Search for files matching pattern"""
    import glob
    return glob.glob(os.path.join(directory, pattern))

def walk(directory):
    """Walk directory tree"""
    result = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            result.append(os.path.join(root, file))
    return result


# ============ Advanced File System Operations ============

def chmod(filepath, mode):
    """Change file permissions"""
    try:
        os.chmod(filepath, mode)
        return True
    except Exception as e:
        raise RuntimeError(f"Permission change error: {e}")

def stat(filepath):
    """Get file statistics"""
    try:
        stats = os.stat(filepath)
        return {
            'size': stats.st_size,
            'created': stats.st_ctime,
            'modified': stats.st_mtime,
            'accessed': stats.st_atime,
            'isFile': os.path.isfile(filepath),
            'isDir': os.path.isdir(filepath)
        }
    except Exception as e:
        raise RuntimeError(f"Stat error: {e}")

def readBinary(filepath):
    """Read file as binary"""
    try:
        with open(filepath, 'rb') as f:
            return f.read()
    except Exception as e:
        raise RuntimeError(f"Binary read error: {e}")

def writeBinary(filepath, data):
    """Write binary data to file"""
    try:
        with open(filepath, 'wb') as f:
            f.write(data)
        return True
    except Exception as e:
        raise RuntimeError(f"Binary write error: {e}")

def rmdir(path):
    """Remove directory"""
    try:
        import shutil
        shutil.rmtree(path)
        return True
    except Exception as e:
        raise RuntimeError(f"Directory remove error: {e}")

def copyDir(source, destination):
    """Copy entire directory"""
    try:
        import shutil
        shutil.copytree(source, destination)
        return True
    except Exception as e:
        raise RuntimeError(f"Directory copy error: {e}")

def tempFile():
    """Create temporary file"""
    import tempfile
    return tempfile.NamedTemporaryFile(delete=False).name

def tempDir():
    """Create temporary directory"""
    import tempfile
    return tempfile.mkdtemp()

def cwd():
    """Get current working directory"""
    return os.getcwd()

def chdir(path):
    """Change current directory"""
    try:
        os.chdir(path)
        return True
    except Exception as e:
        raise RuntimeError(f"Change directory error: {e}")

def home():
    """Get user home directory"""
    return os.path.expanduser("~")

def readCSV(filepath):
    """Read CSV file"""
    try:
        import csv
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            return list(reader)
    except Exception as e:
        raise RuntimeError(f"CSV read error: {e}")

def writeCSV(filepath, data, headers=None):
    """Write CSV file"""
    try:
        import csv
        if not data:
            return False
        
        if headers is None and isinstance(data[0], dict):
            headers = list(data[0].keys())
        
        with open(filepath, 'w', newline='') as f:
            if headers:
                writer = csv.DictWriter(f, fieldnames=headers)
                writer.writeheader()
                writer.writerows(data)
            else:
                writer = csv.writer(f)
                writer.writerows(data)
        return True
    except Exception as e:
        raise RuntimeError(f"CSV write error: {e}")

def hash(filepath, algorithm='sha256'):
    """Calculate file hash"""
    try:
        import hashlib
        h = hashlib.new(algorithm)
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                h.update(chunk)
        return h.hexdigest()
    except Exception as e:
        raise RuntimeError(f"Hash error: {e}")

def compress(source, destination):
    """Compress file/directory to zip"""
    try:
        import shutil
        shutil.make_archive(destination.replace('.zip', ''), 'zip', source)
        return True
    except Exception as e:
        raise RuntimeError(f"Compression error: {e}")

def extract(zipfile, destination):
    """Extract zip file"""
    try:
        import zipfile as zf
        with zf.ZipFile(zipfile, 'r') as zip_ref:
            zip_ref.extractall(destination)
        return True
    except Exception as e:
        raise RuntimeError(f"Extraction error: {e}")

def watch(filepath, callback, interval=1):
    """Watch file for changes"""
    import time
    last_modified = os.path.getmtime(filepath) if os.path.exists(filepath) else 0
    
    while True:
        time.sleep(interval)
        if os.path.exists(filepath):
            current_modified = os.path.getmtime(filepath)
            if current_modified != last_modified:
                callback(filepath)
                last_modified = current_modified
