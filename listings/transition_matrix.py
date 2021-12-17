import pandas as pd
from collections import Counter, defaultdict
from typing import Dict,Union

def transition_matrix(data:pd.DataFrame, state:str="state", prob:bool=True)->Union[Dict,Counter]:
    """
    Compute the transition matrix
    data
        a pandas dataframe
    state
        column name containing the state
        default state
    prob
        return the result as probabilities
        if false, returns the actual count
    """
    values = data[state].values
    c = Counter()
    for i,j in zip(values[:-1], values[1:]):
        c[str(i)+str(j)] +=1
    if prob:
        dct = {}
        total = len(data)-1
        for k,v in c.items():
            dct[k] = v/total
        return dct
    else:
        return c
    

