# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 14:29:51 2022

@author: gulraiz
"""
  
from dummy_API import *
import unittest

class TestTransactions(unittest.TestCase):
    
        
    """tests if balance for given month is correct and is the only transaction"""
    def test_signle_transactions(self):
        d = API()
        d.transactions = {'2022-12-31': 1000}
        self.assertEqual(d.getMonthlyBalance()[12], 1000, "Correct balance")

    
    """tests if balance for given month is correct"""
    def test_multiple_transactions(self):
        d = API()
        d.transactions = {'2022-12-31': 1000, '2022-12-30': 2000}
        self.assertEqual(d.getMonthlyBalance()[12], 3000, "Correct balance")

    
    """tests if balance for multiple months and floating value is correct"""
    def test_multiple_transactions(self):
        d = API()
        d.transactions = {'2022-12-31': 999.99, '2022-1-30': 2000.50, '2022-1-28': 5000.20}
        self.assertEqual(d.getMonthlyBalance()[12], 999.99, "Correct balance")
        self.assertEqual(d.getMonthlyBalance()[1], 7000.70, "Correct balance")

    
      
    """tests if commulative balance for given month is correct and is the only transaction"""
    def test_signle_transactions(self):
        d = API()
        d.transactions = {'2022-12-31': 1000}
        self.assertEqual(d.cumulativeBalance(), 1000, "Correct balance")

    
    """tests if commulative balance for given month is correct"""
    def test_multiple_transactions(self):
        d = API()
        d.transactions = {'2022-12-31': 1000, '2022-12-30': 2000}
        self.assertEqual(d.cumulativeBalance(), 3000, "Correct balance")

    
    """tests if commulative balance for multiple months and floating value is correct"""
    def test_multiple_transactions(self):
        d = API()
        d.transactions = {'2022-12-31': 1000, '2022-1-30': 2000, '2022-1-28': 5000.20}
        self.assertEqual(d.cumulativeBalance(), 8000.20, "Correct balance")


unittest.main()