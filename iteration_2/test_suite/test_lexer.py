from iteration_2.lexer import Lexer
from iteration_2.tokens import *
import pytest


@pytest.mark.parametrize("text,expected", [
    ('1', Token(INTEGER, 1)),
    ('+', Token(PLUS, '+')),
    (')', Token(RPAREN, ')')),

])
def test_single_tokens(text, expected):
    assert Lexer(text).get_next_token() == expected


@pytest.mark.parametrize("text,expected", [
    ('1+2', [
        Token(INTEGER, 1),
        Token(PLUS, '+'),
        Token(INTEGER, 2)
    ]),
    ('(1+2)', [
        Token(LPAREN, '('),
        Token(INTEGER, 1),
        Token(PLUS, '+'),
        Token(INTEGER, 2),
        Token(RPAREN, ')'),
    ]),
    ('(1+2)/5*(1-6)', [
        Token(LPAREN, '('),
        Token(INTEGER, 1),
        Token(PLUS, '+'),
        Token(INTEGER, 2),
        Token(RPAREN, ')'),
        Token(DIV, '/'),
        Token(INTEGER, 5),
        Token(MUL, '*'),
        Token(LPAREN, '('),
        Token(INTEGER, 1),
        Token(MINUS, '-'),
        Token(INTEGER, 6),
        Token(RPAREN, ')')
    ]),
])
def test_multi_tokens(text, expected):
    lexer = Lexer(text)
    for token in expected:
        assert lexer.get_next_token() == token
