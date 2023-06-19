# Loan_repayment

## Content

* [Summary](README.md#Summary)  
* [Project description](README.md#Project-description)  
* [Data and methods](README.md#Data-and-methods)                                
* [Project structure](README.md#Project-structure)                   


---

## Summary

  

## Project description
High competition in the fintech industry pushes companies to innovate. The *LendingClub* company (platform) is the first firm in the US providing peer-to-peer loans between private customers. In addition, the company trades loans on a secondary market. A combination of practical and attractive website, and low interest rates assured fast growth of the client base. This, however, resulted in increase of defaults on the loan repayments rate since current algorythm of the default probability calculation has to be constantly tuned. 

The business objective of the assignment is to identify factors, increasing credit loss of the company such as:
* defaults on the loan repayment
* late installment payments which are subdivided as follows:
    * short overdue (between 16 and 30 days)
    * long overdue (between 31 and 120 days)

An significance estimation of these factors will gradually improves the company profit and provides clients with justified interest rates related to their default risk. 

## Data and methods

Out of a large loan applicantions dataset of 1.6 Gb was taken a sample of some 100,000 entries. The sample contains different applications outcomes which can be seen on the fig.1. To indenitfy negative outcome factors it was selected following distinct categories:
* fully paid
* charged off
* late (31-120 days) and late (16-30 days)

<div align="center"> 
<img src="./figures/fig_1.png" width="500">  </div>

The platform categorizes loans by credit risk as shown on the fig.2. Letters from A to G represents the risk category from the lowest to highest level respectively. Analyzing the chart it can be inferred that the risk categorization smoothly increases by reducing the number of applications. One of risk factors is the loan amount as shown on the fig.3.

<div align="center"><img src="./figures/fig_2.png" width="800">  <img src="./figures/fig_3.png" ></div>


<details>
    <summary>Features description</summary>

text
</details>


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
