import pytest
from plates import is_valid

def test_length():
    assert is_valid("AB") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("ABCDEFG") == False
    assert is_valid("A") == False

def test_startwithletters():
    assert is_valid("AB") == True
    assert is_valid("A1") == False
    assert is_valid("12") == False
    assert is_valid("1A") == False

def test_numbers_placement():
    # Test that numbers are only allowed at the end
    assert is_valid("ABC123") == True
    assert is_valid("AB12C3") == False
    assert is_valid("AB123C") == False

def test_no_leading_zero():
    # Test that numbers do not start with a leading zero
    assert is_valid("AB123") == True
    assert is_valid("AB012") == False

def test_no_punctuation():
    # Test that no punctuation or special characters are allowed
    assert is_valid("AB123") == True
    assert is_valid("AB!123") == False
    assert is_valid("AB-123") == False
    assert is_valid("AB 123") == False
