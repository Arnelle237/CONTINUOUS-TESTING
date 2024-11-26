import sys
import pytest
import io
# Always run from unit_testing_best_practice/test
sys.path += ['../src'] 
from src.password import *
#since the folder src corresponds now to a branch, we should specify it here before the test
#from  password import *

def test_password():
    assert password("abc!/)HUI#123") == "Password is valid!"
