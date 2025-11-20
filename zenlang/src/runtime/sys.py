"""ZenLang sys package - System operations"""
import subprocess
import sys
import os
import time as pytime

def exec(command):
    """Execute system command"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        raise RuntimeError(f"Command execution error: {e}")

def exit(code=0):
    """Exit program"""
    sys.exit(code)

def args():
    """Get command line arguments"""
    return sys.argv[1:]

def env(key):
    """Get environment variable"""
    return os.environ.get(key)

def setenv(key, value):
    """Set environment variable"""
    os.environ[key] = str(value)

def platform():
    """Get platform name"""
    return sys.platform

def version():
    """Get ZenLang version"""
    return "1.0.0"
