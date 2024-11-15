from fuel import convert, gauge
import pytest

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(75) == "75%"
    assert gauge(50) == "50%"

def test_convert():
    assert convert("1/2") == 50
    assert convert("1/100") == 1
    assert convert("4/4") == 100
    assert convert("0/4") == 0

def test_error():
    with pytest.raises(ValueError):
        assert convert("three/four")

    with pytest.raises(ValueError):
        assert convert("5/4")

    with pytest.raises(ZeroDivisionError):
        assert convert("4/0")



