# Loan_repayment

## Content

* [Summary](README.md#Summary)  
* [Project description](README.md#Project-description)  
* [Data and methods](README.md#Data-and-methods)                                
* [Project structure](README.md#Project-structure)                   


---

## Summary

  

## Project description



## Data and methods

The dataset contains information about successful loan applicants which means the loan was approved by the bank. The goal is to identify tendencies leading to:
* default on the loan repayment
* late installment which is subdivided as follows:
    * short overdue (between 16 and 30 days)
    * long overdue (between 31 and 120 days)


<details>
    <summary>Features description</summary>

text
</details>

<div align="center"> 
<img src="./figures/fig.png" width="400">  </div>

<div align="center">  Fig.2   </div>


## Project structure

<details>
  <summary>display project structure </summary>

```Python
Loan_repayment
├── .gitignore
├── config
│   └── config.json     # configuration settings
├── data                # data archive
│  
├── figures
│   ├── fig_1.png
.....
│   └── fig_xx.png
├── models              # models and weights
│   ├── xxx.pkl
.....
│   └── xxx.pkl
├── notebooks           # notebooks
│   └── Loan_repayment.ipynb

├── README.md
├── requirements.txt    
└── utils               # functions and data loaders
    └── reader_config.py
```
</details>
