"""
Created on Tue Nov  2 14:19:05 2022

@author: gulraiz
    - generating a dummy transactions by date for year 2022.
    - balances are values between 0 and 1000.
    - randomly assign balances to each day.
    - compute monthly and commulative balance
    - save data in a json file
    
"""
import json
import pandas as pd
import numpy as np
import datetime

class API:
    
  def __init__(self):
      self.transactions = {}


  def generateTransactions(self):
    days = pd.date_range(start="2022-01-01",end="2022-12-31").to_pydatetime().tolist()
    days = [str(t).split(' ')[0] for t in days]
    balances = np.random.randint(1, 1000, len(days))
    balances = list(map(str, balances))
    
    self.transactions = {tdate:float(amount) for tdate, amount in zip(days, balances)}
    
    
  def getMonthlyBalance(self):
      monthlyBalance ={}
      for tdate in self.transactions:
          datee = datetime.datetime.strptime(tdate, "%Y-%m-%d")
          if datee.month in monthlyBalance:
              monthlyBalance[datee.month]+= self.transactions[tdate]
          else:
              monthlyBalance[datee.month]= self.transactions[tdate]
      
      return monthlyBalance
    
    
  def cumulativeBalance(self):
      return sum(self.transactions.values())
    
          
  def save_file(self):
    with open("transactions.json","w") as f:
        json.dump(self.transactions,f)
        

# if __name__ == "__main__":
#     d = API()
#     d.generateTransactions()
#     d.save_file()
#     print(d.getMonthlyBalance())
#     print(d.cumulativeBalance())
