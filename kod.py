import pytest

def NWD(a, b):
    if a == b:
        return a
    elif a > b:
        return NWD(a - b, b)
    else:
        return NWD(a, b - a)

def test_NWD():
    assert NWD(4,2) == 2
