# Custom functions
import pandas as pd
import numpy as np

features_dscr = pd.read_excel('../data/Features.xlsx', 'LoanStats')

def get_descr(feature:str, feature_names:pd.DataFrame=features_dscr)->str:
    """Get feature description easily

    Args:
        feature (str): feature name

    Returns:
        str: description 
    """
    print(feature_names[feature_names['LoanStatNew']==feature]['Description'].item())