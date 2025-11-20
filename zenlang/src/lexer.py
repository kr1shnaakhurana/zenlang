"""ZenLang Lexer - Tokenizes source code"""
import re
from enum import Enum, auto

class TokenType(Enum):
    # Keywords
    FUNCT = auto()
    IF = auto()
    ELSE = auto()
    WHILE = auto()
    DO = auto()
    FOR = auto()
    BREAK = auto()
    CONTINUE = auto()
    RETURN = auto()
    TRUE = auto()
    FALSE = auto()
    NULL = auto()
    CLASS = auto()
    NEW = auto()
    THIS = auto()
    EXTENDS = auto()
    STATIC = auto()
    PUBLIC = auto()
    PRIVATE = auto()
    PROTECTED = auto()
    
    # Literals
    NUMBER = auto()
    STRING = auto()
    IDENTIFIER = auto()
    
    # Operators
    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    MODULO = auto()
    ASSIGN = auto()
    EQ = auto()
    NEQ = auto()
    LT = auto()
    GT = auto()
    LTE = auto()
    GTE = auto()
    AND = auto()
    OR = auto()
    NOT = auto()
    
    # Delimiters
    LPAREN = auto()
    RPAREN = auto()
    LBRACE = auto()
    RBRACE = auto()
    LBRACKET = auto()
    RBRACKET = auto()
    SEMICOLON = auto()
    COMMA = auto()
    DOT = auto()
    COLON = auto()
    
    # Special
    INCLUDE = auto()
    EOF = auto()

class Token:
    def __init__(self, type, value, line, col):
        self.type = type
        self.value = value
        self.line = line
        self.col = col
    
    def __repr__(self):
        return f"Token({self.type}, {self.value}, {self.line}:{self.col})"

class Lexer:
    def __init__(self, source):
        self.source = source
        self.pos = 0
        self.line = 1
        self.col = 1
        self.tokens = []
        
        self.keywords = {
            'funct': TokenType.FUNCT,
            'if': TokenType.IF,
            'else': TokenType.ELSE,
            'while': TokenType.WHILE,
            'do': TokenType.DO,
            'for': TokenType.FOR,
            'break': TokenType.BREAK,
            'continue': TokenType.CONTINUE,
            'return': TokenType.RETURN,
            'true': TokenType.TRUE,
            'false': TokenType.FALSE,
            'null': TokenType.NULL,
            'class': TokenType.CLASS,
            'new': TokenType.NEW,
            'this': TokenType.THIS,
            'extends': TokenType.EXTENDS,
            'static': TokenType.STATIC,
            'public': TokenType.PUBLIC,
            'private': TokenType.PRIVATE,
            'protected': TokenType.PROTECTED,
        }
    
    def current_char(self):
        if self.pos >= len(self.source):
            return None
        return self.source[self.pos]
    
    def peek(self, offset=1):
        pos = self.pos + offset
        if pos >= len(self.source):
            return None
        return self.source[pos]
    
    def advance(self):
        if self.pos < len(self.source):
            if self.source[self.pos] == '\n':
                self.line += 1
                self.col = 1
            else:
                self.col += 1
            self.pos += 1
    
    def skip_whitespace(self):
        while self.current_char() and self.current_char() in ' \t\n\r':
            self.advance()
    
    def skip_comment(self):
        # Single-line comment with //
        if self.current_char() == '/' and self.peek() == '/':
            while self.current_char() and self.current_char() != '\n':
                self.advance()
            return True
        # Multi-line comment with /* */
        elif self.current_char() == '/' and self.peek() == '*':
            self.advance()
            self.advance()
            while self.current_char():
                if self.current_char() == '*' and self.peek() == '/':
                    self.advance()
                    self.advance()
                    break
                self.advance()
            return True
        # Single-line comment with **
        elif self.current_char() == '*' and self.peek() == '*':
            while self.current_char() and self.current_char() != '\n':
                self.advance()
            return True
        return False
    
    def read_number(self):
        start_col = self.col
        num_str = ''
        while self.current_char() and (self.current_char().isdigit() or self.current_char() == '.'):
            num_str += self.current_char()
            self.advance()
        
        value = float(num_str) if '.' in num_str else int(num_str)
        return Token(TokenType.NUMBER, value, self.line, start_col)
    
    def read_string(self):
        start_col = self.col
        quote = self.current_char()
        self.advance()
        
        string = ''
        while self.current_char() and self.current_char() != quote:
            if self.current_char() == '\\':
                self.advance()
                if self.current_char() == 'n':
                    string += '\n'
                elif self.current_char() == 't':
                    string += '\t'
                elif self.current_char() == '\\':
                    string += '\\'
                elif self.current_char() == quote:
                    string += quote
                else:
                    string += self.current_char()
                self.advance()
            else:
                string += self.current_char()
                self.advance()
        
        self.advance()  # Skip closing quote
        return Token(TokenType.STRING, string, self.line, start_col)
    
    def read_identifier(self):
        start_col = self.col
        ident = ''
        while self.current_char() and (self.current_char().isalnum() or self.current_char() == '_'):
            ident += self.current_char()
            self.advance()
        
        token_type = self.keywords.get(ident, TokenType.IDENTIFIER)
        return Token(token_type, ident, self.line, start_col)
    
    def read_include(self):
        start_col = self.col
        # Skip .include
        while self.current_char() and not self.current_char().isspace():
            self.advance()
        
        self.skip_whitespace()
        
        # Read <package_name>
        if self.current_char() == '<':
            self.advance()
            pkg = ''
            while self.current_char() and self.current_char() != '>':
                pkg += self.current_char()
                self.advance()
            self.advance()  # Skip >
            return Token(TokenType.INCLUDE, pkg, self.line, start_col)
        
        raise SyntaxError(f"Invalid include syntax at {self.line}:{self.col}")
    
    def tokenize(self):
        while self.pos < len(self.source):
            self.skip_whitespace()
            
            if not self.current_char():
                break
            
            if self.skip_comment():
                continue
            
            char = self.current_char()
            col = self.col
            
            # Include directive
            if char == '.' and self.source[self.pos:self.pos+8] == '.include':
                self.tokens.append(self.read_include())
            
            # Numbers
            elif char.isdigit():
                self.tokens.append(self.read_number())
            
            # Strings
            elif char in '"\'':
                self.tokens.append(self.read_string())
            
            # Identifiers and keywords
            elif char.isalpha() or char == '_':
                self.tokens.append(self.read_identifier())
            
            # Operators and delimiters
            elif char == '+':
                self.tokens.append(Token(TokenType.PLUS, '+', self.line, col))
                self.advance()
            elif char == '-':
                self.tokens.append(Token(TokenType.MINUS, '-', self.line, col))
                self.advance()
            elif char == '*':
                self.tokens.append(Token(TokenType.MULTIPLY, '*', self.line, col))
                self.advance()
            elif char == '/':
                self.tokens.append(Token(TokenType.DIVIDE, '/', self.line, col))
                self.advance()
            elif char == '%':
                self.tokens.append(Token(TokenType.MODULO, '%', self.line, col))
                self.advance()
            elif char == '=':
                if self.peek() == '=':
                    self.tokens.append(Token(TokenType.EQ, '==', self.line, col))
                    self.advance()
                    self.advance()
                else:
                    self.tokens.append(Token(TokenType.ASSIGN, '=', self.line, col))
                    self.advance()
            elif char == '!':
                if self.peek() == '=':
                    self.tokens.append(Token(TokenType.NEQ, '!=', self.line, col))
                    self.advance()
                    self.advance()
                else:
                    self.tokens.append(Token(TokenType.NOT, '!', self.line, col))
                    self.advance()
            elif char == '<':
                if self.peek() == '=':
                    self.tokens.append(Token(TokenType.LTE, '<=', self.line, col))
                    self.advance()
                    self.advance()
                else:
                    self.tokens.append(Token(TokenType.LT, '<', self.line, col))
                    self.advance()
            elif char == '>':
                if self.peek() == '=':
                    self.tokens.append(Token(TokenType.GTE, '>=', self.line, col))
                    self.advance()
                    self.advance()
                else:
                    self.tokens.append(Token(TokenType.GT, '>', self.line, col))
                    self.advance()
            elif char == '&' and self.peek() == '&':
                self.tokens.append(Token(TokenType.AND, '&&', self.line, col))
                self.advance()
                self.advance()
            elif char == '|' and self.peek() == '|':
                self.tokens.append(Token(TokenType.OR, '||', self.line, col))
                self.advance()
                self.advance()
            elif char == '(':
                self.tokens.append(Token(TokenType.LPAREN, '(', self.line, col))
                self.advance()
            elif char == ')':
                self.tokens.append(Token(TokenType.RPAREN, ')', self.line, col))
                self.advance()
            elif char == '{':
                self.tokens.append(Token(TokenType.LBRACE, '{', self.line, col))
                self.advance()
            elif char == '}':
                self.tokens.append(Token(TokenType.RBRACE, '}', self.line, col))
                self.advance()
            elif char == ';':
                self.tokens.append(Token(TokenType.SEMICOLON, ';', self.line, col))
                self.advance()
            elif char == ',':
                self.tokens.append(Token(TokenType.COMMA, ',', self.line, col))
                self.advance()
            elif char == '.':
                self.tokens.append(Token(TokenType.DOT, '.', self.line, col))
                self.advance()
            elif char == '[':
                self.tokens.append(Token(TokenType.LBRACKET, '[', self.line, col))
                self.advance()
            elif char == ']':
                self.tokens.append(Token(TokenType.RBRACKET, ']', self.line, col))
                self.advance()
            elif char == ':':
                self.tokens.append(Token(TokenType.COLON, ':', self.line, col))
                self.advance()
            else:
                raise SyntaxError(f"Unexpected character '{char}' at {self.line}:{col}")
        
        self.tokens.append(Token(TokenType.EOF, None, self.line, self.col))
        return self.tokens
