"""ZenLang zenout package - I/O operations"""

def console(*args):
    """Print to console"""
    print(*args)

def input(prompt=""):
    """Read input from user"""
    import builtins
    return builtins.input(prompt)

def log(*args):
    """Log message"""
    print("[LOG]", *args)

def error(*args):
    """Print error message"""
    print("[ERROR]", *args)

def warn(*args):
    """Print warning message"""
    print("[WARN]", *args)
