import sys
import pandas as pd
import pytest
from collections import Counter
sys.path.append('listings')

from transition_matrix import *

@pytest.fixture
def matrix():
    return pd.read_excel('tests/transition.xls', sheet_name='raw')

def test_transition_matrix(matrix):
    result = {('a', 'a'):0.3, ('a','b'):0.3, ('b','a'):0.2, ('b','b'):0.2}
    assert transition_matrix(matrix) == result

def test_transition_matrix_count(matrix):
    result = {('a', 'a'):3, ('a','b'):3, ('b','a'):2, ('b','b'):2}
    assert transition_matrix(matrix,prob=False) == result

