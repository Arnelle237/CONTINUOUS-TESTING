import sys
# Always run from unit_testing_best_practice/test
sys.path += ['../src'] 

from username import *

def test_user_name():
    #assert test_user_name=="hui man!h"
    assert user_name("hui234")== "hui234"