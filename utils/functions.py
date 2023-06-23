# Custom functions
import pandas as pd
import numpy as np
import os

from utils.config_reader import config_reader 
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, roc_auc_score


# Импортируем константы из файла config
config = config_reader('../config/config.json')
path_figures = config.path_figures

features_dscr = pd.read_excel('../data/Features.xlsx') #, sheetname='LoanStats'

def get_descr(feature:str, feature_names:pd.DataFrame=features_dscr)->str:
    """Get feature description easily

    Args:
        feature (str): feature name

    Returns:
        str: description 
    """
    print(feature_names[feature_names['LoanStatNew']==feature]['Description'].item())


def get_ROC_plot(model,  X_test, y_test, title:str,  plot_counter:int=None):
    """
    Create the roc curve plot
    Args:
        model (_type_): pre-trained model to get prediction
        X_test (_type_): X matrice with 
        y_test (_type_): y predicted values
        title (_type_): _description_
        figpath (_int_): figure path for saving
    """
    y_pred = model.predict_proba(X_test)[:,1]
    metric = roc_auc_score(y_test, y_pred).round(3)
    print('roc_auc: ', metric)

    false_positive_rates, true_positive_rates, threshold = roc_curve(y_test, y_pred)


    # Plot
    fig, ax = plt.subplots(figsize=(5, 5))

    # ROC curve
    ax.plot(false_positive_rates, true_positive_rates, 
            label='Smoothed values ROC-AUC')

    # Random model
    ax.plot([0, 1], [0, 1], color='k', lw=2, linestyle=':', 
            label='Model predicting random')

    ax.set_xlabel('False Positive Rate')
    ax.set_ylabel('True Positive Rate')

    ax.fill_between(false_positive_rates, 
                    true_positive_rates, 
                    step="pre", 
                    alpha=0.4, label='Area under curve (ROC-AUC)')
    
    # Annotate figure with ROC curve
    plt.annotate(f'ROC: {metric}', 
        xy=(0.45,0.6), textcoords='data', 
        bbox={'facecolor': 'w', 'alpha': 0.95, 'pad': 10} 
    );
    
    ax.legend()
    
    
    if plot_counter is not None:
        ax.set_title(f'Fig.{plot_counter} - ROC curve for {title}', y=-0.25,fontsize=13, loc='center')
        plt.tight_layout()
        plt.savefig(path_figures + f'fig_{plot_counter}.png')
        
    else:
        #plot_counter=1
        plt.tight_layout()
        ax.set_title(f'ROC curve for {title}', y=-0.25)- 
        
        
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
        

def get_professions(arg:str)->str:
    """Categorization of popular professions

    Args:
        arg (str): строка датафрейма

    Returns:
        _type_: _description_
    """    
    
    arg = arg.lower().replace('/',' ')
    
    management = ['foreman','shop foreman', 'team leader','chef','maintenance supervisor','team lead','administration', 'deputy', 'forman', 'superviser','administrative', 'admin','group leader','manger', 'crew leader', 'mgr','payroll', 'superintendant', 'superintendent']
    executives = ['general manager', 'vice president','director','account executive', 'sales executive','ceo', 'partner', 'president','senior vice president', 'vp','svp','cfo','cto', 'gm', 'coo','co-owner', 'vp of operations', 'vp operations', 'senior associate', 'co-founder', 'founder']
    #engineers = ['engineer','software engineer']

    employees = ['nurse', 'registered nurse', 'rn', 'lpn', 'cna', 'nursing','social worker', 'bartender', 'cook', 'machinist', 'bookkeeper','machine operator','electrician', 'operator', 'carpenter', 'pharmacist','clerk','cashier','laborer','receptionist','instructor','welder','dispatcher','bus operator', 'custodian', 'underwriter', 'realtor','conductor','mechanic','firefighter','maintenance','server','production','flight attendant', 'designer','security', 'lvn','buyer', 'agent','service tech','plumber','warehouse', 'stylist','hairstylist', 'teller', 'pastor','senior pastor','clerical','courier', 'logistics', 'shipping','transportation','porter', 'material handler','labor','painter','lineman','assembly', 'contractor','data entry','housekeeping','office','librarian','sous chef', 'nanny', 'installer','warehouse worker','assembler','table games dealer', 'adjuster', 'firefighter paramedic','millwright','baker','merchandiser','doorman','barista']
    
    skilled_laborers = ['engineer', 'officer','administrative assistant', 'administrator','paralegal', 'attorney', 'counselor','cse','supervisor', 'csr','pilot','ramp agent', 'captain','investigator','service advisor', 'human resources','at&t','recruiter', 'hr','housekeeper', \
        # law
        'lawyer', 'auditor', 
        #IT
        'it', 'programmer','software developer','it specialist','web developer','coder',
        #finance
        'banker', 'bank of america','accounts payable','medical biller','controller', 'accounting', 'personal banker','broker','business development','loan processor','financial advisor','payroll specialist','jp morgan chase','stocker','relationship banker','estimator','mortgage banker','finance','biller','accounts receivable','cpa','cma','billing','account representative', 'wells fargo', 'northrop grumman',
        # education
        'professor','teacher', 'educator', 'faculty','dean','paraprofessional','lecturer',
        #security
        'security guard','lieutenant','united states air force','sergeant', 'inspector','staff sergeant', 'deputy sheriff','border patrol agent', 'detective','special agent','us army','major', 'department of defense','lockheed martin','us air force','us navy','detective','u.s. army',
        # sales
        'sales rep','sales', 'sales representative','dealer','purchasing','collector', 'purchasing agent', \
        # medics
        'physician', 'dental hygienist','pharmacy tech', 'paramedic', 'caregiver','dentist','phlebotomist', 'optician','psychologist','speech language pathologist','resident physician', 'veterinarian','respiratory therapist', 'care giver','kaiser permanente','radiographer', 'clinician', \
        # other
        'advisor','trainer','claims adjuster', 'principal', 'associate','graphic designer','marketing', 'quality control','lead','chemist','specialist','scientist','operations',
        ]
    #sales = []
    

    if arg in executives or 'owner' in arg or 'president' in arg: 
        return 'executive' 
    
    elif arg in management or 'manager' in arg or 'supervisor' in arg or 'executive' in arg or 'coordinator' in arg or 'lead' in arg or 'foreman' in arg or 'forman' in arg or 'head' in arg or 'supervisior' in arg or 'director' in arg or 'mgr' in arg or 'management' in arg or 'managing' in arg:   
        return 'manager'
    
    elif arg in skilled_laborers or 'consultant' in arg or 'analyst' in arg or 'officer' in arg or 'engineer' in arg or 'accountant' in arg or 'bank' in arg or 'administrator' in arg or 'counselor' in arg or 'insurance' in arg or 'police' in arg or 'it' in arg or 'professor' in arg or 'teacher' in arg or 'specialist' in arg or 'programmer' in arg or 'scientist' in arg or 'developer' in arg or 'coder' in arg or 'psychologist' in arg or 'therapist' in arg or 'pathologist' in arg or 'emt' in arg or 'agent' in arg or 'officer' in arg or 'attorney' in arg or 'paralegal' in arg or 'minister' in arg or 'research' in arg or 'buyer' in arg or 'billing' in arg or 'associate' in arg or 'planner' in arg or 'representative' in arg or 'professional' in arg or 'broker' in arg or 'trainer' in arg or 'admin' in arg:
        return 'skilled_laborer'
    
    elif arg in employees or 'technician' in arg or 'operator' in arg or 'assistant' in arg or 'nurse' in arg or 'tech' in arg or 'sales' in arg  or 'service' in arg or 'controller' in arg or 'mail' in arg or 'ups' in arg or 'usps' in arg or 'post' in arg or 'staff' in arg or 'worker' in arg or 'clerk' in arg or 'mechanic' in arg or 'carrier' in arg or 'machinist' in arg or 'desk' in arg or 'manufacturing' in arg or 'driver' in arg or 'handler' in arg or 'secretary' in arg or 'dispatcher' in arg or 'electrician' in arg:
        return 'employee'
   
    else:
        return 'other' #arg
    
    
def get_sigma_limits(data: pd.DataFrame, features:list, sigma_factor=3):
    """Returns upper limit 

    Args:
        feature (pd.DataFrame): Feature to process
        limit
    """    
    for i, name in enumerate(features):
        mean = data[name].mean()
        std = data[name].std() 
        upper_limit = round(mean + sigma_factor* std)
        lower_limit = round(mean - sigma_factor* std)
        #print(f'Upper limit for {name} is: ', upper_limit)
        
        n_outliers = len(data[(data['annual_inc_log'] < lower_limit) | (data['annual_inc_log'] > upper_limit)].index)
        print('number of outliers: ', n_outliers)
        
        limits = {'upper_limit':upper_limit,
                  'lower_limit':lower_limit,
                  'n_outliers': n_outliers}
        
    return limits