"""ZenLang time package - Time operations"""
import time as pytime

def now():
    """Get current timestamp"""
    return pytime.time()

def sleep(seconds):
    """Sleep for specified seconds"""
    pytime.sleep(seconds)

def date():
    """Get current date/time string"""
    return pytime.strftime("%Y-%m-%d %H:%M:%S")

def timestamp():
    """Get current Unix timestamp"""
    return int(pytime.time())
