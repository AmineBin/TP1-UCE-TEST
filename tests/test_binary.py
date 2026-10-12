from unittest.mock import patch
import pytest
import random

# Binary
def test_binary_value_match():
    value = random.randint(1, 100)
    result = encode(value) 
    assert decode(result) == value

def test_binary_value_unmatch():
    value = 5
    result = "0010"
    assert decode(result) != value

def test_binary_value_zero():
    value = 0
    result = encode(value)
    assert decode(result) == value

def test_binary_negative_value():
    value = -5
    result = encode(value)
    assert decode(result) == value

def test_binary_decimal_value():
    with pytest.raises((TypeError, ValueError)):
        encode(5.3)

def test_binary_invalid_characters():
    with pytest.raises((TypeError, ValueError)):
        decode("jizj")

def test_binary_invalid_length():
    with pytest.raises((TypeError, ValueError)):
        decode("010")