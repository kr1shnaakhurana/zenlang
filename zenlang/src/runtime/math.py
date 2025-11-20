"""ZenLang math package - Mathematical operations"""
import math as pymath
import random as pyrandom

def abs(x):
    """Absolute value"""
    return pymath.fabs(x)

def sqrt(x):
    """Square root"""
    return pymath.sqrt(x)

def pow(x, y):
    """Power"""
    return pymath.pow(x, y)

def floor(x):
    """Floor"""
    return pymath.floor(x)

def ceil(x):
    """Ceiling"""
    return pymath.ceil(x)

def round(x):
    """Round"""
    return pymath.round(x)

def sin(x):
    """Sine"""
    return pymath.sin(x)

def cos(x):
    """Cosine"""
    return pymath.cos(x)

def tan(x):
    """Tangent"""
    return pymath.tan(x)

def random():
    """Random number between 0 and 1"""
    return pyrandom.random()

def randint(a, b):
    """Random integer between a and b"""
    return pyrandom.randint(a, b)

def max(*args):
    """Maximum value"""
    return max(*args)

def min(*args):
    """Minimum value"""
    return min(*args)

# Constants
PI = pymath.pi
E = pymath.e
