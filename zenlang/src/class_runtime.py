"""ZenLang Class Runtime System"""

class ZenClass:
    """Represents a class definition in ZenLang"""
    def __init__(self, name, parent, methods, properties, static_methods, static_properties):
        self.name = name
        self.parent = parent
        self.methods = methods  # Dict of method_name -> list of MethodDef (for overloading)
        self.properties = properties  # Dict of property_name -> PropertyDef
        self.static_methods = static_methods
        self.static_properties = static_properties
    
    def get_method(self, name, arg_count):
        """Get method by name and argument count (for overloading)"""
        if name in self.methods:
            # Find method with matching parameter count
            for method in self.methods[name]:
                if len(method.params) == arg_count:
                    return method
            # If no exact match, return first one (fallback)
            return self.methods[name][0] if self.methods[name] else None
        
        # Check parent class
        if self.parent:
            return self.parent.get_method(name, arg_count)
        
        return None
    
    def get_static_method(self, name, arg_count):
        """Get static method by name and argument count"""
        if name in self.static_methods:
            for method in self.static_methods[name]:
                if len(method.params) == arg_count:
                    return method
            return self.static_methods[name][0] if self.static_methods[name] else None
        
        if self.parent:
            return self.parent.get_static_method(name, arg_count)
        
        return None
    
    def has_property(self, name):
        """Check if property exists"""
        return name in self.properties or (self.parent and self.parent.has_property(name))
    
    def get_property(self, name):
        """Get property definition"""
        if name in self.properties:
            return self.properties[name]
        if self.parent:
            return self.parent.get_property(name)
        return None


class ZenInstance:
    """Represents an instance of a ZenLang class"""
    def __init__(self, zen_class):
        self.zen_class = zen_class
        self.properties = {}
        
        # Initialize instance properties from class
        for prop_name, prop_def in zen_class.properties.items():
            if not prop_def.is_static:
                self.properties[prop_name] = None
    
    def get_property(self, name):
        """Get property value with access control"""
        if name in self.properties:
            return self.properties[name]
        
        # Check class property
        prop_def = self.zen_class.get_property(name)
        if prop_def and prop_def.is_static:
            return prop_def.value
        
        raise AttributeError(f"Property '{name}' not found")
    
    def set_property(self, name, value, caller_context='public'):
        """Set property value with access control"""
        prop_def = self.zen_class.get_property(name)
        
        if prop_def:
            # Check access modifier
            if prop_def.access_modifier == 'private' and caller_context != 'internal':
                raise AttributeError(f"Cannot access private property '{name}'")
            
            if prop_def.is_static:
                prop_def.value = value
            else:
                self.properties[name] = value
        else:
            # Dynamic property
            self.properties[name] = value
    
    def call_method(self, name, args, interpreter, caller_context='public'):
        """Call instance method with overloading support"""
        method = self.zen_class.get_method(name, len(args))
        
        if not method:
            raise AttributeError(f"Method '{name}' with {len(args)} arguments not found")
        
        # Check access modifier
        if method.access_modifier == 'private' and caller_context != 'internal':
            raise AttributeError(f"Cannot access private method '{name}'")
        
        # Create method environment with 'this' binding
        from src.interpreter import Environment, ReturnException
        method_env = Environment(parent=interpreter.global_env)
        method_env.set('this', self)
        
        # Bind parameters
        for i, param in enumerate(method.params):
            method_env.set(param, args[i] if i < len(args) else None)
        
        # Execute method body
        try:
            interpreter.eval(method.body, method_env)
            return None
        except ReturnException as e:
            return e.value
    
    def __repr__(self):
        return f"<{self.zen_class.name} instance>"
