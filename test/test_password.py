import sys
import pytest
import io
# Always run from unit_testing_best_practice/test
sys.path += ['../src'] 

from  password import *

def test_password():
    assert password("abc!/)HUI#123") == "Password is valid!"