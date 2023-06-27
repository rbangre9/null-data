import numpy as np 
import pandas as pd

def process_null_percentage(col):
    column_len = len(col)
    null_count = col.isnull().sum()
    return "{:.2f}".format((null_count / column_len) * 100) + "%"

def nulls(data):
    numColumns = data.shape[1]
    return {i : process_null_percentage(data.iloc[:, i]) for i in range (numColumns)}