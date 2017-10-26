from myself.my_calc import Lexer, Token, INTEGER, PLUS, MINUS, MUL, DIV
import pytest


# @pytest.fixture
# def create_lexer(test_input):
#     return Lexer(test_input)


@pytest.mark.parametrize("text,expected", [
    ("3", Token(INTEGER, 3)),
    ("+", Token(PLUS, '+')),
    ("/", Token(DIV, '/')),
])
def test_single_token(text, expected):
    assert Lexer(text).get_next_token().value == expected.value
    # :TODO: compare Token type


@pytest.mark.parametrize("text,expected", [
    ("1+2", [Token(INTEGER, 1), Token(PLUS, '+'), Token(INTEGER, 2)]),
])
def test_single_token(text, expected):
    lexer = Lexer(text)
    for token in expected:
        assert lexer.get_next_token().value == token.value
    # :TODO: compare Token type