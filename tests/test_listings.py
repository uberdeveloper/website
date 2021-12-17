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
    assert transition_matrix(matrix) == {'aa':0.3,'ab':0.3,'ba':0.2,'bb':0.2}

def test_transition_matrix_count(matrix):
    assert transition_matrix(matrix,prob=False) == {'aa':3,'ab':3,'ba':2,'bb':2}

