# Project-4
Link to our site: http://cc-approval.herokuapp.com/


## Overview
Due to COVID-19, many people have lost their jobs, resulting in people strapping for cash and defaulting on their credit card payments. Things have gotten so bad that credit card companies, such as JP Morgan and Citigroup have to set aside an additional reserve to cover their losses from credit card defaults¹. Now, this is a very extreme case, which does not happen often (I really hope not). People’s inability to pay for their credit card bills could be due to different circumstances. However, when it’s deliberate, meaning that customers have no plans in paying the bank back, it would be considered as a fraud. Either way, this imposes a huge risk on the credit card companies and we need to find a way to flag them.


To address this issue, we can predict potential default accounts based on certain attributes. The idea is that the earlier the potential default accounts are detected, the lower the losses we will embrace. On the other hand, we can be proactive by providing tips to customers to prevent default. This not only protects our customers but also minimizes our risks and potential losses.


## Goal
To predict whether the customer will default on their credit card payment next month.


## Motivation
There are times when even a seemingly manageable debt, such as credit cards, goes out of control. Loss of job, medical crisis or business failure are some of the reasons that can impact your finances. In fact, credit card debts are usually the first to get out of hand in such situations due to hefty finance charges (compounded on daily balances) and other penalties.

A lot of us would be able to relate to this scenario. We may have missed credit card payments once or twice because of forgotten due dates or cash flow issues. But what happens when this continues for months? How to predict if a customer will be defaulter in next months?

To reduce the risk of Banks, this model has been developed to predict customer defaulter based on demographic data like gender, age, marital status and behavioral data like last payments, past transactions etc.




## **Technologies**

- Python (Jupyter Notebook, Pandas)
- Flask 
- SQL/ Postgres DB
- JavaScript Libraries 
- HTML/ CSS (Bootstrap)
- Csv
- Machine Learning



These are the steps: 
1. Data Cleaning
    - Removing extraneous columns
    - Null values
    - Duplicates
    - Merging datasets by grouping shows
2. Individual scatter plots for each feature
3. Regularization: Coefficient plots with Linear Regression
4. Function to test the familiar Regressors
5. Scaling the data – StandScaler & MinMaxScaler
6. Model Selection & Prediction
7. MSE & R-squared score: Lesson Learnt 
8. Exported the model -> Flask implementation
