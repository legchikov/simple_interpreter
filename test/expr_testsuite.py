from myself.my_calc import Interpreter, Lexer
import pytest


@pytest.mark.parametrize("text,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 54),
])
def test_one_operator(text, expected):
    assert Interpreter(Lexer(text)).expr() == expected


@pytest.mark.parametrize("text,expected", [
    ("3 + 5", 8),
    (" 2+4", 6),
    ("6*9 ", 54),
    (" 3 + 5 ", 8),
    (" 2+    4", 6),
    ("   6   *   9   ", 54),
])
def test_one_operator_with_space(text, expected):
    assert Interpreter(Lexer(text)).expr() == expected


@pytest.mark.parametrize("text,expected", [
    ("1+2+3+4", 10),
    ("1*2*3*4", 24),
    ("10-20+30-100", -80),
])
def test_multi_operator(text, expected):
    assert Interpreter(Lexer(text)).expr() == expected


@pytest.mark.parametrize("text,expected", [
    ("1+2*3+4", 11),
    ("1*2+3*4", 14),
    ("10-20+30-100", -80),
])
def test_mix_operator(text, expected):
    assert Interpreter(Lexer(text)).expr() == expected

