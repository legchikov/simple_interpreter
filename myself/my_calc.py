
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

    def eat(self, token_type):
        print('eat:', self.current_token)
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()

    def expr(self):
        self.current_token = self.get_next_token()
        left = self.current_token
        self.eat(INTEGER)

        op = self.current_token
        if op.type == PLUS:
            self.eat(PLUS)
        elif op.type == MINUS:
            self.eat(MINUS)
        elif op.type == MUL:
            self.eat(MUL)
        else:
            self.eat(DIV)

        right = self.current_token
        self.eat(INTEGER)
        if op.type == PLUS:
            result = left.value + right.value
        elif op.type == MINUS:
            result = left.value - right.value
        elif op.type == MUL:
            result = left.value * right.value
        else:
            result = left.value / right.value

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
        result = lexer.expr()
        print(str(result))

        # interpreter = Interpreter(lexer)
        # result = interpreter.expr()
        # print(str(result))

        '''
        print(lexer.get_next_token())
        print(lexer.get_next_token())
        print(lexer.get_next_token())
        print(lexer.get_next_token())
        print(lexer.get_next_token())
        '''


if __name__ == '__main__':
    main()

