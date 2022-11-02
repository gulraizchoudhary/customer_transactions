#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 14:19:05 2022

@author: gulraiz

 - must run in terminal.
 - monthly balance: input 1-12 as a month of the year 2022, returns balance of the month. 
     will calucalate the summation of balances from 1st of Jan untill 20th of Feb.
        
"""
import sys
from dummy_API import *

d = API()
d.generateTransactions()


month = sys.argv[1]

print("Your Balance for the Month of"+month+" : "+d.getMonthlyBalance()[month])
print("Your Cummulative Balance: "+d.cumulativeBalance())
