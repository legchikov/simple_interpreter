
INTEGER, PLUS, MINUS, MUL, DIV, EOF = 'INTEGER', 'PLUS', 'MINUS', 'MUL', 'DIV', 'EOF'


class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return 'Token ({type}, {value})'.format(
            type=self.type,
            value=self.value
        )


class Lexer(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]
        self.current_token = None

    def error(self):
        raise Exception('Lexer error')

    def advance(self):
        self.pos += 1

        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

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

            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')

            if self.current_char == '*':
                self.advance()
                return Token(MUL, '*')

            if self.current_char == '/':
                self.advance()
                return Token(DIV, '/')

        return Token(EOF, None)


class Interpreter:
    def __init__(self, lexer):
        self.lexer = lexer

    def eat(self, token_type):
        print('eat:', self.lexer.current_token)
        if self.lexer.current_token.type == token_type:
            self.lexer.current_token = self.lexer.get_next_token()

    def expr(self):

        self.lexer.current_token = self.lexer.get_next_token()
        result = self.lexer.current_token.value
        self.eat(INTEGER)

        while self.lexer.current_token.type in (PLUS, MINUS, MUL, DIV):
            op = self.lexer.current_token

            if op.type == PLUS:
                self.eat(PLUS)
            elif op.type == MINUS:
                self.eat(MINUS)
            elif op.type == MUL:
                self.eat(MUL)
            else:
                self.eat(DIV)

            right = self.lexer.current_token
            self.eat(INTEGER)

            if op.type == PLUS:
                result += right.value
            elif op.type == MINUS:
                result -= right.value
            elif op.type == MUL:
                result *= right.value
            else:
                result /= right.value

        return result


def main():
    while True:
        try:
            text = input('legchikov> ')
        except EOFError:
            break
        if not text:
            continue
        lexer = Lexer(text)
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        print(str(result))

if __name__ == '__main__':
    main()

