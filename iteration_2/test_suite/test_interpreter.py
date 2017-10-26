from iteration_2.lexer import Lexer
from iteration_2.interpreter import Interpreter
import pytest

# :TODO: Negative test cases


@pytest.mark.parametrize("text,expected", [
    ('1+2', 3),
    ('2*3', 6),
    ('10/5', 2),
    ('15-4', 11)
])
def test_single_expression(text, expected):
    assert Interpreter(Lexer(text)).expr() == expected


@pytest.mark.parametrize("text,expected", [
    ('1+2+3+4+5', 15),
    ('2*3*4/2', 12),
    ('1+2*3-1', 6),
    ('15-4', 11)
])
def test_multi_expression(text, expected):
    assert Interpreter(Lexer(text)).expr() == expected


@pytest.mark.parametrize("text,expected", [
    ('1  +  2', 3),
    ('  2  *3', 6),
    ('   10    /    5    ', 2),
    ('15-4     ', 11)
])
def test_spaces_expression(text, expected):
    assert Interpreter(Lexer(text)).expr() == expected


@pytest.mark.parametrize("text,expected", [
    ('1+2-(3+4)+5', 1),
    ('2*3*4/2*(1+2+3)', 72),
    ('(1+2)*(3-1)', 6),
    ('((1+2)*(2+3))/((1+2+3)-1)-5', -2)
])
def test_parenthesis_expression(text, expected):
    assert Interpreter(Lexer(text)).expr() == expected