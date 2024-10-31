import pytest
from twttr import shorten

def test_A():
    assert shorten("dad") == "dd"

def test_E():
    assert shorten("Teeth") == "Tth"

def test_I():
    assert shorten("inch") == "nch"

def test_O():
    assert shorten("God") == "Gd"

def test_U():
    assert shorten("Under") == "ndr"

def test_AEIOU():
    assert shorten("Givenchy") == "Gvnchy"

def test_number():
    assert shorten("CS50") == "CS50"

def test_punc():
    assert shorten("What's your name?") == "Wht's yr nm?"



