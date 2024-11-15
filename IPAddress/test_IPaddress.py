import pytest
from numb3rs import validate

def test_validate_regular_ip():
    assert validate("127.0.0.1") == True

def test_validate_max():
    assert validate("255.255.255.255") == True

def test_validate_out_of_range():
    assert validate("512.512.512.512") == False

def test_validate_last_out_of_range():
    assert validate("1.2.3.1000") == False

def test_validate_word():
    assert validate("cat") == False

def test_validate_first_byte():
    assert validate("999.1.1.1") == False
    assert validate("1.999.1.1") == False
    assert validate("1.1.999.1") == False
    assert validate("1.1.1.999") == False
    assert validate("1.1.1.1") == True