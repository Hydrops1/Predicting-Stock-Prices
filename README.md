# What is the goal of the project
## The goal of this tool is to provide information on whether a stock price of certain company will rise or fall. 
# Who will be able to benefit from it
It is designed for investors, stock market speculators, or anyone who seeks help in predicting value of stocks of companies.
# Returned information
## Prediction of the change of stock price of a given company. The range of certain classes are the following:
```Bash
-10% >= stock change [%] - 0 (sharp decline)
-10% < stock change [%] < 0 - 1 (small decline)
0% <= stock change[%] < 10% - 2 (small growth)
10% <= stock change [%] - 3 (sharp growth)

Note: The ranges may change. The project in the future might have more functions, but for now we focus on those aforementioned.
```
