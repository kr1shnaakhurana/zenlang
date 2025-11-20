"""ZenLang Parser - Builds AST from tokens"""
from src.lexer import TokenType
from src.ast import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
    
    def current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return self.tokens[-1]  # EOF
    
    def peek(self, offset=1):
        pos = self.pos + offset
        if pos < len(self.tokens):
            return self.tokens[pos]
        return self.tokens[-1]
    
    def advance(self):
        self.pos += 1
    
    def expect(self, token_type):
        token = self.current_token()
        if token.type != token_type:
            raise SyntaxError(f"Expected {token_type}, got {token.type} at {token.line}:{token.col}")
        self.advance()
        return token
    
    def parse(self):
        includes = []
        statements = []
        
        # Parse includes
        while self.current_token().type == TokenType.INCLUDE:
            includes.append(self.parse_include())
        
        # Parse statements
        while self.current_token().type != TokenType.EOF:
            stmt = self.parse_statement()
            if stmt is not None:  # Skip None statements (empty statements)
                statements.append(stmt)
        
        return Program(includes, statements)
    
    def parse_include(self):
        token = self.expect(TokenType.INCLUDE)
        return Include(token.value)
    
    def parse_statement(self):
        token = self.current_token()
        
        if token.type == TokenType.CLASS:
            return self.parse_class_def()
        elif token.type == TokenType.FUNCT:
            return self.parse_function_def()
        elif token.type == TokenType.IF:
            return self.parse_if()
        elif token.type == TokenType.WHILE:
            return self.parse_while()
        elif token.type == TokenType.DO:
            return self.parse_do_while()
        elif token.type == TokenType.FOR:
            return self.parse_for()
        elif token.type == TokenType.BREAK:
            self.advance()
            self.expect(TokenType.SEMICOLON)
            return Break()
        elif token.type == TokenType.CONTINUE:
            self.advance()
            self.expect(TokenType.SEMICOLON)
            return Continue()
        elif token.type == TokenType.RETURN:
            return self.parse_return()
        elif token.type == TokenType.LBRACE:
            return self.parse_block()
        else:
            return self.parse_expression_statement()
    
    def parse_function_def(self, require_semicolon=True):
        self.expect(TokenType.FUNCT)
        
        # Check if named or anonymous
        name = None
        if self.current_token().type == TokenType.IDENTIFIER:
            name = self.current_token().value
            self.advance()
        
        self.expect(TokenType.LPAREN)
        params = []
        
        while self.current_token().type != TokenType.RPAREN:
            params.append(self.expect(TokenType.IDENTIFIER).value)
            if self.current_token().type == TokenType.COMMA:
                self.advance()
        
        self.expect(TokenType.RPAREN)
        body = self.parse_block()
        
        # Only require semicolon for top-level function definitions
        if require_semicolon:
            self.expect(TokenType.SEMICOLON)
        
        return FunctionDef(name, params, body)
    
    def parse_if(self):
        self.expect(TokenType.IF)
        self.expect(TokenType.LPAREN)
        condition = self.parse_expression()
        self.expect(TokenType.RPAREN)
        then_block = self.parse_block()
        
        else_block = None
        if self.current_token().type == TokenType.ELSE:
            self.advance()
            # Check for 'else if' pattern
            if self.current_token().type == TokenType.IF:
                # Treat 'else if' as nested if statement
                else_block = Block([self.parse_if()])
            else:
                else_block = self.parse_block()
        
        return If(condition, then_block, else_block)
    
    def parse_while(self):
        self.expect(TokenType.WHILE)
        self.expect(TokenType.LPAREN)
        condition = self.parse_expression()
        self.expect(TokenType.RPAREN)
        body = self.parse_block()
        
        return While(condition, body)
    
    def parse_do_while(self):
        self.expect(TokenType.DO)
        body = self.parse_block()
        self.expect(TokenType.WHILE)
        self.expect(TokenType.LPAREN)
        condition = self.parse_expression()
        self.expect(TokenType.RPAREN)
        self.expect(TokenType.SEMICOLON)
        
        return DoWhile(body, condition)
    
    def parse_for(self):
        self.expect(TokenType.FOR)
        self.expect(TokenType.LPAREN)
        
        # Init statement
        init = None
        if self.current_token().type != TokenType.SEMICOLON:
            init = self.parse_expression()
        self.expect(TokenType.SEMICOLON)
        
        # Condition
        condition = None
        if self.current_token().type != TokenType.SEMICOLON:
            condition = self.parse_expression()
        self.expect(TokenType.SEMICOLON)
        
        # Increment
        increment = None
        if self.current_token().type != TokenType.RPAREN:
            increment = self.parse_expression()
        self.expect(TokenType.RPAREN)
        
        body = self.parse_block()
        
        return For(init, condition, increment, body)
    
    def parse_return(self):
        self.expect(TokenType.RETURN)
        value = None
        if self.current_token().type != TokenType.SEMICOLON:
            value = self.parse_expression()
        self.expect(TokenType.SEMICOLON)
        return Return(value)
    
    def parse_block(self):
        self.expect(TokenType.LBRACE)
        statements = []
        
        while self.current_token().type != TokenType.RBRACE:
            stmt = self.parse_statement()
            if stmt is not None:  # Skip None statements (empty statements)
                statements.append(stmt)
        
        self.expect(TokenType.RBRACE)
        return Block(statements)
    
    def parse_expression_statement(self):
        # Handle empty statements (just semicolon)
        if self.current_token().type == TokenType.SEMICOLON:
            self.advance()
            return None
        
        expr = self.parse_expression()
        self.expect(TokenType.SEMICOLON)
        return expr
    
    def parse_expression(self):
        return self.parse_assignment()
    
    def parse_assignment(self):
        expr = self.parse_logical_or()
        
        if self.current_token().type == TokenType.ASSIGN:
            # Check if it's a simple identifier assignment
            if isinstance(expr, Identifier):
                self.advance()
                value = self.parse_assignment()
                return Assignment(expr.name, value)
            # Check if it's an index assignment (arr[i] = value)
            elif isinstance(expr, IndexAccess):
                self.advance()
                value = self.parse_assignment()
                return IndexAssignment(expr.array, expr.index, value)
            # Check if it's a member assignment (obj.prop = value)
            elif isinstance(expr, MemberAccess):
                self.advance()
                value = self.parse_assignment()
                return MemberAssignment(expr.object, expr.member, value)
            else:
                raise SyntaxError("Invalid assignment target")
        
        return expr
    
    def parse_logical_or(self):
        left = self.parse_logical_and()
        
        while self.current_token().type == TokenType.OR:
            op = self.current_token().value
            self.advance()
            right = self.parse_logical_and()
            left = BinaryOp(left, op, right)
        
        return left
    
    def parse_logical_and(self):
        left = self.parse_equality()
        
        while self.current_token().type == TokenType.AND:
            op = self.current_token().value
            self.advance()
            right = self.parse_equality()
            left = BinaryOp(left, op, right)
        
        return left
    
    def parse_equality(self):
        left = self.parse_comparison()
        
        while self.current_token().type in (TokenType.EQ, TokenType.NEQ):
            op = self.current_token().value
            self.advance()
            right = self.parse_comparison()
            left = BinaryOp(left, op, right)
        
        return left
    
    def parse_comparison(self):
        left = self.parse_additive()
        
        while self.current_token().type in (TokenType.LT, TokenType.GT, TokenType.LTE, TokenType.GTE):
            op = self.current_token().value
            self.advance()
            right = self.parse_additive()
            left = BinaryOp(left, op, right)
        
        return left
    
    def parse_additive(self):
        left = self.parse_multiplicative()
        
        while self.current_token().type in (TokenType.PLUS, TokenType.MINUS):
            op = self.current_token().value
            self.advance()
            right = self.parse_multiplicative()
            left = BinaryOp(left, op, right)
        
        return left
    
    def parse_multiplicative(self):
        left = self.parse_unary()
        
        while self.current_token().type in (TokenType.MULTIPLY, TokenType.DIVIDE, TokenType.MODULO):
            op = self.current_token().value
            self.advance()
            right = self.parse_unary()
            left = BinaryOp(left, op, right)
        
        return left
    
    def parse_unary(self):
        if self.current_token().type in (TokenType.NOT, TokenType.MINUS):
            op = self.current_token().value
            self.advance()
            operand = self.parse_unary()
            return UnaryOp(op, operand)
        
        return self.parse_postfix()
    
    def parse_postfix(self):
        expr = self.parse_primary()
        
        while True:
            if self.current_token().type == TokenType.DOT:
                self.advance()
                member = self.expect(TokenType.IDENTIFIER).value
                
                # Check if it's a method call
                if self.current_token().type == TokenType.LPAREN:
                    self.advance()
                    args = []
                    while self.current_token().type != TokenType.RPAREN:
                        args.append(self.parse_expression())
                        if self.current_token().type == TokenType.COMMA:
                            self.advance()
                    self.expect(TokenType.RPAREN)
                    expr = FunctionCall(MemberAccess(expr, member), args)
                else:
                    expr = MemberAccess(expr, member)
            
            elif self.current_token().type == TokenType.LPAREN:
                self.advance()
                args = []
                while self.current_token().type != TokenType.RPAREN:
                    args.append(self.parse_expression())
                    if self.current_token().type == TokenType.COMMA:
                        self.advance()
                self.expect(TokenType.RPAREN)
                expr = FunctionCall(expr, args)
            
            elif self.current_token().type == TokenType.LBRACKET:
                self.advance()
                index = self.parse_expression()
                self.expect(TokenType.RBRACKET)
                expr = IndexAccess(expr, index)
            
            else:
                break
        
        return expr
    
    def parse_primary(self):
        token = self.current_token()
        
        if token.type == TokenType.NUMBER:
            self.advance()
            return Literal(token.value)
        
        elif token.type == TokenType.STRING:
            self.advance()
            return Literal(token.value)
        
        elif token.type == TokenType.IDENTIFIER:
            self.advance()
            return Identifier(token.value)
        
        elif token.type == TokenType.LPAREN:
            self.advance()
            expr = self.parse_expression()
            self.expect(TokenType.RPAREN)
            return expr
        
        elif token.type == TokenType.LBRACE:
            return self.parse_object_literal()
        
        elif token.type == TokenType.LBRACKET:
            return self.parse_array_literal()
        
        elif token.type == TokenType.FUNCT:
            # Anonymous function in expression - don't require semicolon
            return self.parse_function_def(require_semicolon=False)
        
        elif token.type == TokenType.TRUE:
            self.advance()
            return Literal(True)
        
        elif token.type == TokenType.FALSE:
            self.advance()
            return Literal(False)
        
        elif token.type == TokenType.NULL:
            self.advance()
            return Literal(None)
        
        elif token.type == TokenType.NEW:
            return self.parse_new_instance()
        
        elif token.type == TokenType.THIS:
            self.advance()
            return ThisExpression()
        
        else:
            raise SyntaxError(f"Unexpected token {token.type} at {token.line}:{token.col}")
    
    def parse_object_literal(self):
        self.expect(TokenType.LBRACE)
        properties = {}
        
        while self.current_token().type != TokenType.RBRACE:
            key = self.expect(TokenType.IDENTIFIER).value
            self.expect(TokenType.ASSIGN)
            value = self.parse_expression()
            properties[key] = value
            
            if self.current_token().type == TokenType.COMMA:
                self.advance()
        
        self.expect(TokenType.RBRACE)
        return ObjectLiteral(properties)
    
    def parse_array_literal(self):
        self.expect(TokenType.LBRACKET)
        elements = []
        
        while self.current_token().type != TokenType.RBRACKET:
            elements.append(self.parse_expression())
            
            if self.current_token().type == TokenType.COMMA:
                self.advance()
        
        self.expect(TokenType.RBRACKET)
        return ArrayLiteral(elements)

    
    def parse_class_def(self):
        """Parse class definition with methods and properties"""
        self.expect(TokenType.CLASS)
        class_name = self.expect(TokenType.IDENTIFIER).value
        
        # Check for inheritance
        parent = None
        if self.current_token().type == TokenType.EXTENDS:
            self.advance()
            parent = self.expect(TokenType.IDENTIFIER).value
        
        self.expect(TokenType.LBRACE)
        
        methods = []
        properties = []
        
        while self.current_token().type != TokenType.RBRACE:
            # Parse access modifiers
            access_modifier = 'public'
            is_static = False
            
            if self.current_token().type in [TokenType.PUBLIC, TokenType.PRIVATE, TokenType.PROTECTED]:
                access_modifier = self.current_token().value
                self.advance()
            
            if self.current_token().type == TokenType.STATIC:
                is_static = True
                self.advance()
            
            # Check if it's a method or property
            if self.current_token().type == TokenType.FUNCT:
                method = self.parse_method_def(access_modifier, is_static)
                methods.append(method)
            else:
                # Property definition
                prop_name = self.expect(TokenType.IDENTIFIER).value
                prop_value = None
                
                if self.current_token().type == TokenType.ASSIGN:
                    self.advance()
                    prop_value = self.parse_expression()
                
                self.expect(TokenType.SEMICOLON)
                properties.append(PropertyDef(prop_name, prop_value, access_modifier, is_static))
        
        self.expect(TokenType.RBRACE)
        return ClassDef(class_name, parent, methods, properties)
    
    def parse_method_def(self, access_modifier='public', is_static=False):
        """Parse method definition within a class"""
        self.expect(TokenType.FUNCT)
        method_name = self.expect(TokenType.IDENTIFIER).value
        
        self.expect(TokenType.LPAREN)
        params = []
        
        while self.current_token().type != TokenType.RPAREN:
            param = self.expect(TokenType.IDENTIFIER).value
            params.append(param)
            
            if self.current_token().type == TokenType.COMMA:
                self.advance()
        
        self.expect(TokenType.RPAREN)
        body = self.parse_block()
        
        return MethodDef(method_name, params, body, access_modifier, is_static)

    
    def parse_new_instance(self):
        """Parse new instance creation"""
        self.expect(TokenType.NEW)
        class_name = self.expect(TokenType.IDENTIFIER).value
        
        self.expect(TokenType.LPAREN)
        args = []
        
        while self.current_token().type != TokenType.RPAREN:
            args.append(self.parse_expression())
            
            if self.current_token().type == TokenType.COMMA:
                self.advance()
        
        self.expect(TokenType.RPAREN)
        return NewInstance(class_name, args)
