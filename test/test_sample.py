import sys
# Always run from unit_testing_best_practice/test
sys.path += ['../src'] 

from sample import *

def test_answer():
  assert func(4) == 5 #work fine beacause func(4) = 5 so test passed
  #assert func(3) == 5  # failed cause 4#5