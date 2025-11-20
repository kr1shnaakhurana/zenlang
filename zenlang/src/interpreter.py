"""ZenLang Interpreter - Executes AST"""
import os
from src.ast import *
from src.class_runtime import ZenClass, ZenInstance

class BreakException(Exception):
    pass

class ContinueException(Exception):
    pass

class ReturnException(Exception):
    def __init__(self, value):
        self.value = value

class Environment:
    def __init__(self, parent=None):
        self.vars = {}
        self.parent = parent
    
    def get(self, name):
        if name in self.vars:
            return self.vars[name]
        elif self.parent:
            return self.parent.get(name)
        else:
            raise NameError(f"Variable '{name}' not defined")
    
    def set(self, name, value):
        self.vars[name] = value
    
    def exists(self, name):
        return name in self.vars or (self.parent and self.parent.exists(name))

class ZenFunction:
    def __init__(self, name, params, body, closure, interpreter):
        self.name = name
        self.params = params
        self.body = body
        self.closure = closure
        self.interpreter = interpreter
    
    def __call__(self, *args):
        """Make ZenFunction callable from Python"""
        # Create new environment for function
        func_env = Environment(self.closure)
        for param, arg in zip(self.params, args):
            func_env.set(param, arg)
        
        try:
            self.interpreter.eval(self.body, func_env)
            return None
        except ReturnException as e:
            return e.value

class Interpreter:
    def __init__(self):
        self.global_env = Environment()
        self.packages = {}
        self.load_builtin_packages()
    
    def load_builtin_packages(self):
        from src.runtime import zenout, net, fs, web, sys as zensys, math as zenmath, time as zentime, zenin, zenwares, builtins as zenbuiltins, zenweb, zendb, zengui, zenhttp
        
        self.packages['zenout'] = zenout
        self.packages['net'] = net
        self.packages['fs'] = fs
        self.packages['web'] = web
        self.packages['sys'] = zensys
        self.packages['math'] = zenmath
        self.packages['time'] = zentime
        self.packages['zenin'] = zenin
        self.packages['zenwares'] = zenwares
        self.packages['zenweb'] = zenweb
        self.packages['zendb'] = zendb
        self.packages['zengui'] = zengui
        self.packages['http'] = zenhttp
        
        # Load built-in functions into global scope
        self.load_builtins(zenbuiltins)
    
    def load_builtins(self, builtins_module):
        """Load built-in functions into global environment"""
        builtin_functions = [
            # Type conversion
            'str', 'int', 'float', 'bool',
            # Type checking
            'type', 'isNumber', 'isString', 'isArray', 'isObject', 'isBool', 'isNull',
            # Array functions
            'length', 'push', 'pop', 'shift', 'unshift', 'slice', 'indexOf', 
            'includes', 'reverse', 'sort', 'join', 'filter', 'map',
            # String functions
            'upper', 'lower', 'trim', 'split', 'replace', 'startsWith', 
            'endsWith', 'substring', 'charAt', 'repeat',
            # Math functions
            'sum', 'avg', 'min', 'max',
            # Object functions
            'keys', 'values', 'hasKey',
            # Utility functions
            'range', 'print', 'input',
            # Advanced array functions
            'flatten', 'chunk', 'zip', 'unique', 'compact', 'difference', 
            'intersection', 'union',
            # Advanced string functions
            'capitalize', 'titleCase', 'count', 'padStart', 'padEnd', 
            'truncate', 'slugify', 'contains',
            # Object/Dict functions
            'merge', 'pick', 'omit', 'entries', 'fromEntries',
            # Number functions
            'clamp', 'lerp', 'random', 'randomInt', 'round', 'abs', 'sign',
            # Utility functions
            'sleep', 'timestamp', 'formatNumber', 'parseJSON', 'toJSON', 
            'deepCopy', 'isEmpty', 'isEqual', 'clone',
            # Functional programming
            'forEach', 'reduce', 'every', 'some', 'find', 'findIndex',
            'groupBy', 'sortBy', 'take', 'drop', 'takeWhile', 'dropWhile',
            'partition', 'pluck', 'countBy', 'sample', 'shuffle', 'times',
            # Higher-order functions
            'debounce', 'throttle', 'memoize', 'curry', 'compose', 'pipe',
            'noop', 'identity', 'constant', 'negate', 'once'
        ]
        
        for func_name in builtin_functions:
            if hasattr(builtins_module, func_name):
                self.global_env.set(func_name, getattr(builtins_module, func_name))
    
    def run(self, program):
        # Load includes
        for include in program.includes:
            self.load_include(include)
        
        # Execute statements
        for stmt in program.statements:
            self.eval(stmt, self.global_env)
    
    def load_include(self, include_node):
        pkg_name = include_node.package
        
        # Check if it's a local script
        if '/' in pkg_name:
            # Try multiple paths
            paths_to_try = [
                pkg_name + '.zen',  # Relative to current directory
                os.path.join('zenlang', pkg_name + '.zen'),  # Relative to zenlang folder
                os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', pkg_name + '.zen')  # Relative to interpreter
            ]
            
            script_path = None
            for path in paths_to_try:
                if os.path.exists(path):
                    script_path = path
                    break
            
            if script_path:
                with open(script_path, 'r') as f:
                    source = f.read()
                from src.lexer import Lexer
                from src.parser import Parser
                lexer = Lexer(source)
                tokens = lexer.tokenize()
                parser = Parser(tokens)
                ast = parser.parse()
                self.run(ast)
            else:
                raise ImportError(f"Script not found: {pkg_name}.zen (tried: {', '.join(paths_to_try)})")
        else:
            # Load package
            if pkg_name in self.packages:
                self.global_env.set(pkg_name, self.packages[pkg_name])
            else:
                # Try to load from ~/.zenpkgs/
                pkg_path = os.path.expanduser(f"~/.zenpkgs/{pkg_name}")
                if os.path.exists(pkg_path):
                    # Load package (simplified)
                    pass
                else:
                    raise ImportError(f"Package not found: {pkg_name}")
    
    def eval(self, node, env):
        if isinstance(node, Program):
            for stmt in node.statements:
                self.eval(stmt, env)
        
        elif isinstance(node, FunctionDef):
            func = ZenFunction(node.name, node.params, node.body, env, self)
            if node.name:
                env.set(node.name, func)
            return func
        
        elif isinstance(node, ClassDef):
            return self.eval_class_def(node, env)
        
        elif isinstance(node, NewInstance):
            return self.eval_new_instance(node, env)
        
        elif isinstance(node, ThisExpression):
            return env.get('this')
        
        elif isinstance(node, FunctionCall):
            func = self.eval(node.name, env)
            args = [self.eval(arg, env) for arg in node.args]
            
            if isinstance(func, ZenFunction):
                # Create new environment for function
                func_env = Environment(func.closure)
                for param, arg in zip(func.params, args):
                    func_env.set(param, arg)
                
                try:
                    self.eval(func.body, func_env)
                    return None
                except ReturnException as e:
                    return e.value
            
            elif callable(func):
                return func(*args)
            
            else:
                raise TypeError(f"'{func}' is not callable")
        
        elif isinstance(node, MemberAccess):
            obj = self.eval(node.object, env)
            
            if isinstance(obj, ZenInstance):
                # Handle instance property/method access
                try:
                    return obj.get_property(node.member)
                except AttributeError:
                    # Return a bound method
                    # Check if calling from within the same instance (this.method())
                    caller_context = 'internal' if isinstance(node.object, ThisExpression) else 'public'
                    return lambda *args: obj.call_method(node.member, args, self, caller_context)
            elif isinstance(obj, ZenClass):
                # Handle static method/property access
                if node.member in obj.static_properties:
                    return obj.static_properties[node.member].value
                elif node.member in obj.static_methods:
                    # Return static method
                    return lambda *args: self.call_static_method(obj, node.member, args, env)
                else:
                    raise AttributeError(f"Class '{obj.name}' has no static member '{node.member}'")
            elif isinstance(obj, dict):
                return obj.get(node.member)
            elif hasattr(obj, node.member):
                return getattr(obj, node.member)
            else:
                raise AttributeError(f"Object has no member '{node.member}'")
        
        elif isinstance(node, Assignment):
            value = self.eval(node.value, env)
            env.set(node.name, value)
            return value
        
        elif isinstance(node, MemberAssignment):
            obj = self.eval(node.object, env)
            value = self.eval(node.value, env)
            
            if isinstance(obj, ZenInstance):
                obj.set_property(node.member, value, 'internal')
            elif isinstance(obj, dict):
                obj[node.member] = value
            else:
                raise TypeError(f"Cannot set property on {type(obj)}")
            
            return value
        
        elif isinstance(node, BinaryOp):
            left = self.eval(node.left, env)
            right = self.eval(node.right, env)
            
            if node.op == '+':
                # Handle string concatenation - convert to string if either operand is string
                if isinstance(left, str) or isinstance(right, str):
                    return str(left) + str(right)
                return left + right
            elif node.op == '-':
                return left - right
            elif node.op == '*':
                return left * right
            elif node.op == '/':
                return left / right
            elif node.op == '%':
                return left % right
            elif node.op == '==':
                return left == right
            elif node.op == '!=':
                return left != right
            elif node.op == '<':
                return left < right
            elif node.op == '>':
                return left > right
            elif node.op == '<=':
                return left <= right
            elif node.op == '>=':
                return left >= right
            elif node.op == '&&':
                return left and right
            elif node.op == '||':
                return left or right
        
        elif isinstance(node, UnaryOp):
            operand = self.eval(node.operand, env)
            
            if node.op == '-':
                return -operand
            elif node.op == '!':
                return not operand
        
        elif isinstance(node, Literal):
            return node.value
        
        elif isinstance(node, Identifier):
            return env.get(node.name)
        
        elif isinstance(node, Block):
            for stmt in node.statements:
                self.eval(stmt, env)
        
        elif isinstance(node, If):
            condition = self.eval(node.condition, env)
            if condition:
                self.eval(node.then_block, env)
            elif node.else_block:
                self.eval(node.else_block, env)
        
        elif isinstance(node, While):
            while self.eval(node.condition, env):
                try:
                    self.eval(node.body, env)
                except BreakException:
                    break
                except ContinueException:
                    continue
        
        elif isinstance(node, DoWhile):
            while True:
                try:
                    self.eval(node.body, env)
                except BreakException:
                    break
                except ContinueException:
                    pass
                
                if not self.eval(node.condition, env):
                    break
        
        elif isinstance(node, Break):
            raise BreakException()
        
        elif isinstance(node, Continue):
            raise ContinueException()
        
        elif isinstance(node, Return):
            value = self.eval(node.value, env) if node.value else None
            raise ReturnException(value)
        
        elif isinstance(node, ObjectLiteral):
            obj = {}
            for key, value_node in node.properties.items():
                obj[key] = self.eval(value_node, env)
            return obj
        
        elif isinstance(node, ArrayLiteral):
            return [self.eval(elem, env) for elem in node.elements]
        
        elif isinstance(node, IndexAccess):
            array = self.eval(node.array, env)
            index = self.eval(node.index, env)
            
            if isinstance(array, (list, str)):
                try:
                    return array[int(index)]
                except (IndexError, ValueError) as e:
                    raise RuntimeError(f"Index error: {e}")
            elif isinstance(array, dict):
                return array.get(str(index))
            else:
                raise TypeError(f"Cannot index {type(array)}")
        
        elif isinstance(node, IndexAssignment):
            # Get the array
            array_name = node.array.name if isinstance(node.array, Identifier) else None
            if not array_name:
                raise RuntimeError("Can only assign to indexed variables")
            
            array = env.get(array_name)
            index = self.eval(node.index, env)
            value = self.eval(node.value, env)
            
            if isinstance(array, list):
                try:
                    array[int(index)] = value
                except (IndexError, ValueError) as e:
                    raise RuntimeError(f"Index assignment error: {e}")
            elif isinstance(array, dict):
                array[str(index)] = value
            else:
                raise TypeError(f"Cannot assign to index of {type(array)}")
            
            return value
        
        elif isinstance(node, For):
            # Initialize
            if node.init:
                self.eval(node.init, env)
            
            # Loop
            while True:
                # Check condition
                if node.condition:
                    if not self.eval(node.condition, env):
                        break
                
                # Execute body
                try:
                    self.eval(node.body, env)
                except BreakException:
                    break
                except ContinueException:
                    pass
                
                # Increment
                if node.increment:
                    self.eval(node.increment, env)
        
        return None

    
    def eval_class_def(self, node, env):
        """Evaluate class definition with method overloading support"""
        # Get parent class if exists
        parent_class = None
        if node.parent:
            parent_class = env.get(node.parent)
            if not isinstance(parent_class, ZenClass):
                raise TypeError(f"'{node.parent}' is not a class")
        
        # Organize methods by name (for overloading)
        methods = {}
        static_methods = {}
        
        for method in node.methods:
            if method.is_static:
                if method.name not in static_methods:
                    static_methods[method.name] = []
                static_methods[method.name].append(method)
            else:
                if method.name not in methods:
                    methods[method.name] = []
                methods[method.name].append(method)
        
        # Organize properties
        properties = {}
        static_properties = {}
        
        for prop in node.properties:
            prop_value = self.eval(prop.value, env) if prop.value else None
            prop.value = prop_value  # Store evaluated value
            
            if prop.is_static:
                static_properties[prop.name] = prop
            else:
                properties[prop.name] = prop
        
        # Create class object
        zen_class = ZenClass(node.name, parent_class, methods, properties, static_methods, static_properties)
        env.set(node.name, zen_class)
        
        return zen_class
    
    def eval_new_instance(self, node, env):
        """Create new instance of a class"""
        zen_class = env.get(node.class_name)
        
        if not isinstance(zen_class, ZenClass):
            raise TypeError(f"'{node.class_name}' is not a class")
        
        # Create instance
        instance = ZenInstance(zen_class)
        
        # Initialize properties with default values
        for prop_name, prop_def in zen_class.properties.items():
            if not prop_def.is_static and prop_def.value is not None:
                instance.properties[prop_name] = prop_def.value
        
        # Call constructor if exists
        args = [self.eval(arg, env) for arg in node.args]
        constructor = zen_class.get_method(node.class_name, len(args))
        
        if constructor:
            # Create constructor environment with 'this' binding
            constructor_env = Environment(parent=self.global_env)
            constructor_env.set('this', instance)
            
            # Bind parameters
            for i, param in enumerate(constructor.params):
                constructor_env.set(param, args[i] if i < len(args) else None)
            
            # Execute constructor
            try:
                self.eval(constructor.body, constructor_env)
            except ReturnException:
                pass  # Constructors don't return values
        
        return instance

    
    def call_static_method(self, zen_class, method_name, args, env):
        """Call static method"""
        method = zen_class.get_static_method(method_name, len(args))
        
        if not method:
            raise AttributeError(f"Static method '{method_name}' with {len(args)} arguments not found")
        
        # Create method environment
        method_env = Environment(parent=self.global_env)
        
        # Bind parameters
        for i, param in enumerate(method.params):
            method_env.set(param, args[i] if i < len(args) else None)
        
        # Execute method
        try:
            self.eval(method.body, method_env)
            return None
        except ReturnException as e:
            return e.value
