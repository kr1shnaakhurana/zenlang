"""ZenLang AST Node Definitions"""

class ASTNode:
    pass

class Program(ASTNode):
    def __init__(self, includes, statements):
        self.includes = includes
        self.statements = statements

class Include(ASTNode):
    def __init__(self, package):
        self.package = package

class FunctionDef(ASTNode):
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

class FunctionCall(ASTNode):
    def __init__(self, name, args):
        self.name = name
        self.args = args

class MemberAccess(ASTNode):
    def __init__(self, object, member):
        self.object = object
        self.member = member

class Assignment(ASTNode):
    def __init__(self, name, value):
        self.name = name
        self.value = value

class BinaryOp(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class UnaryOp(ASTNode):
    def __init__(self, op, operand):
        self.op = op
        self.operand = operand

class Literal(ASTNode):
    def __init__(self, value):
        self.value = value

class Identifier(ASTNode):
    def __init__(self, name):
        self.name = name

class Block(ASTNode):
    def __init__(self, statements):
        self.statements = statements

class If(ASTNode):
    def __init__(self, condition, then_block, else_block=None):
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block

class While(ASTNode):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class DoWhile(ASTNode):
    def __init__(self, body, condition):
        self.body = body
        self.condition = condition

class Break(ASTNode):
    pass

class Continue(ASTNode):
    pass

class Return(ASTNode):
    def __init__(self, value=None):
        self.value = value

class ObjectLiteral(ASTNode):
    def __init__(self, properties):
        self.properties = properties  # dict of key: value

class ArrayLiteral(ASTNode):
    def __init__(self, elements):
        self.elements = elements  # list of expressions

class IndexAccess(ASTNode):
    def __init__(self, array, index):
        self.array = array
        self.index = index

class IndexAssignment(ASTNode):
    def __init__(self, array, index, value):
        self.array = array
        self.index = index
        self.value = value

class For(ASTNode):
    def __init__(self, init, condition, increment, body):
        self.init = init
        self.condition = condition
        self.increment = increment
        self.body = body


# Class-related AST nodes
class ClassDef(ASTNode):
    def __init__(self, name, parent, methods, properties):
        self.name = name
        self.parent = parent  # For inheritance
        self.methods = methods  # List of MethodDef
        self.properties = properties  # List of PropertyDef

class MethodDef(ASTNode):
    def __init__(self, name, params, body, access_modifier='public', is_static=False):
        self.name = name
        self.params = params
        self.body = body
        self.access_modifier = access_modifier  # 'public', 'private', 'protected'
        self.is_static = is_static

class PropertyDef(ASTNode):
    def __init__(self, name, value=None, access_modifier='public', is_static=False):
        self.name = name
        self.value = value
        self.access_modifier = access_modifier
        self.is_static = is_static

class NewInstance(ASTNode):
    def __init__(self, class_name, args):
        self.class_name = class_name
        self.args = args

class ThisExpression(ASTNode):
    pass


class MemberAssignment(ASTNode):
    def __init__(self, object, member, value):
        self.object = object
        self.member = member
        self.value = value
