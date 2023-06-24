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

### Current credit risk policy

There is no information provided about whether the credit risk assessment policy of the company was changed over time. Analyzing growing default rates and overdue rates over time shown on the fig.2, however, it can be stated that the company had beed issuing more and more risky loans until 2015. Even though the annual default rate has substantially droped form 31% to 18% since 2016, the overdue rate has soared from 2 to 20%. A perilous credit policy resulted in a substantial financial loss.

<div align="center"> 
<img src="./figures/fig_2.png" width="450"> </div>

### Features analysis
<details>
  <summary>Features analysis </summary>
The platform categorizes loans by credit risk as shown on the fig.3. Letters from A to G represents the risk category from the lowest to highest level respectively. Analyzing the graph it can be inferred that default rate  smoothly increases by category. Surprisingly, default rate in the group 'G' exceeds Categories B and C contains the majority of all applications (slightly more 30% each).

<div align="center"><img src="./figures/fig_3.png" width="500">  </div>

Customers with lower loan grades repay their loans more often in contrast to those with higher loan grades. It implies that the lower the loan ammount the higher probablility of repayment without delay. Taking into account the loans terms distribution shown on the fig.4, it can be added that short-term loans have lower probability of default or overdue. 

<div align="center"> 
<img src="./figures/fig_4.png" width="500">  </div>

The default rate slightly decreases from 30% to 25% when applicant's employment duration reaches 2 years, and afterwards remains stable around 25% as shown on the fig.5. Taking into account loan applicants job titles shown on the fig.6 it can be said, that skilled laborers have lower default probability in contrast to that of other job titles. Notably that overdue rate is equal to 3 % for every job title.  

<div align="center"> 
<img src="./figures/fig_5.png" width="440"><img src="./figures/fig_6.png" width="440">  </div>

Applicants with lower annual incomes are more prone to defaul unlike those with larger annual incomes as shown on the fig.7. Probably financial difficulties affect borrowers' ability to repay their loans. The feature yet contains multiple outliers exceeding the range of $mean \pm 3 * st.diviation$.

<div align="center"> 
<img src="./figures/fig_7.png" width="440"> </div>

Analyzing the number of years since the first recorded credit up to the moment when the loan was request from the company shown on the fig.8 it can be inferred:
* the borrower's default rate substantially dropps from 40% to 30% after 3 years since the first credit and then gradually downwards to 18% unil the credit history span reaches 35 years. Then it starts to grow and fluctuating significantly.
* similarly to the default rate, overdue rate reamins stable at 2% until the credit history span reaches 35 years, and then constanly increases by 1% annualy.

<div align="center"> <img src="./figures/fig_8.png" width="500"> </div>

</details>

## ML model
The gradien boosting model was applied to identify hidden interrelationship between features. The model classifies default accounts from fully paid ones with high precision as showh on the fig.9.

<div align="center"> 
<img src="./figures/fig_9.png" width="350"> <img src="./figures/fig_10.png" width="450"></div>

It is essential that the interest rate is the most significant factor of the default as shown on the fig.10. In case the employment duration is fewer than 10 years, the probability of default is higher. The longer the credit history span, the lower the default rate. It is fair until the span reaches 35 years. Lower loan is far easier to repay as usual.

The rate, however, is calculated using multiple multiples. Two major factors, which positively correlates with the rate are employment duration and the loan amount. 
Obviously the company  consider applicants' as reliable in case their credit history is long. The default rate, however, would be lower in case the credit history span will be within the range of 3 and 35 years.

<div align="center"> <img src="./figures/fig_11.png" width="600"> </div>

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
