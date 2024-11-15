from bank import value
import pytest

def test_hello():
    assert value("Hello") == 0

def test_hellomore():
    assert value("hello, Newman") == 0

def test_lower():
    assert value("how are you") == 20

def test_h():
    assert value("How you doing?") == 20

def test_others():
    assert value("What's up") == 100

def test_space():
    assert value(" what's hanging>") == 100
