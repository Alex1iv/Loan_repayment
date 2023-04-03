# Custom functions
import pandas as pd
import numpy as np
import os

from utils.config_reader import config_reader 
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, roc_auc_score


# Импортируем константы из файла config
config = config_reader('../config/config.json')

features_dscr = pd.read_excel('../data/Features.xlsx', 'LoanStats')

def get_descr(feature:str, feature_names:pd.DataFrame=features_dscr)->str:
    """Get feature description easily

    Args:
        feature (str): feature name

    Returns:
        str: description 
    """
    print(feature_names[feature_names['LoanStatNew']==feature]['Description'].item())
    
def get_comparison(models:dict, X_test, y_test, path_figures=config.path_figures, fig_id:int=None): #title:str, 
    """
    Plot roc curves of given models from dictionary.
    Args:
        model (_dict_): pre-trained models dictionary
        X_test (_type_): X matrice with test values
        y_test (_type_): y predicted values
        figpath (_int_): figure path for saving
    """
    # Plot
    fig, ax = plt.subplots(figsize=(5, 5))

    # Random model
    ax.plot([0, 1], [0, 1], color='k', lw=2, linestyle=':', 
            label='Random classifier')

    for name, model in models.items():
        y_pred = model.predict_proba(X_test)[:,1]
        metric = roc_auc_score(y_test, y_pred).round(3)
        
        false_positive_rates, true_positive_rates, threshold = roc_curve(y_test, y_pred)

        # ROC curve
        ax.plot(false_positive_rates, true_positive_rates, label=f'{name}')

    ax.set_title(f'Fig.{fig_id} - Models comparison by ROC curves', y=-0.2) 
    ax.set_xlabel('False Positive Rate')
    ax.set_ylabel('True Positive Rate')

    ax.legend()
    plt.tight_layout();
    
    if fig_id:
        plt.savefig(os.path.join(path_figures + f'fig_{fig_id}.png'))