from iteration_2.tokens import *
import pytest


@pytest.mark.parametrize("token_type,value,expected", [
    (INTEGER, 8, Token(INTEGER, 8)),
    (INTEGER, 123, Token(INTEGER, 123)),
    (INTEGER, 55588811, Token(INTEGER, 55588811)),
    (PLUS, '+', Token(PLUS, '+')),
    (MINUS, '-', Token(MINUS, '-')),
    (MUL, '*', Token(MUL, '*')),
    (DIV, '/', Token(DIV, '/')),
    (LPAREN, '(', Token(LPAREN, '(')),
    (RPAREN, ')', Token(RPAREN, ')')),
    (EOF, None, Token(EOF, None))
])
def test_tokens(token_type, value, expected):
    assert Token(token_type, value) == expected
