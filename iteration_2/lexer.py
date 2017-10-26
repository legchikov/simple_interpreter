from iteration_2.tokens import *


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Invalid syntax')

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_spaces(self):
        while self.current_char and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.current_char and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):

        while self.current_char:
            if self.current_char.isspace():
                self.skip_spaces()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())
            elif self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')
            elif self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')
            elif self.current_char == '*':
                self.advance()
                return Token(MUL, '*')
            elif self.current_char == '/':
                self.advance()
                return Token(DIV, '/')
            elif self.current_char == '(':
                self.advance()
                return Token(LPAREN, '(')
            elif self.current_char == ')':
                self.advance()
                return Token(RPAREN, ')')

            self.error()

        return Token(EOF, None)