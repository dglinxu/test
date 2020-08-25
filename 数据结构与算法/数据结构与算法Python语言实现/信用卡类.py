#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 开发人员：dglin     创建时间：2020/6/7
# 开发工具：PyCharm   文件名称：CreditCard.py
# E-mail: humen@189.cn
'''说明： 
----------------------------'''


class CreditCard:
    """消费者信用卡"""

    def __init__(self, customer, bank, acnt, limit):
        """生成一个新信用卡实例

        The initial balance is zero.

        customer  the name of the customer(e.g.,'John Bowman')
        bank      the name of the bank(e.g.,'CAlifornia Savings')
        acnt      the acount identifier (e.g.,5391 0375 93875309')
        limit     credit limit (measured in dollars)
        """

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0     #余额

    def get_customer(self):
        """返回消费者名字"""
        return self._customer

    def get_bank(self):
        """返回银行的名字"""
        return self._bank

    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self._account

    def get_limit(self):
        """返回当前信用卡限额"""
        return self._limit

    def get_balance(self):
        """Return current balance"""
        return self._balance

    def charge(self,price):
        """Charge giver price to the card,assuming sufficient credit limit.

        Return True if charge(收费） wos processed;False if charge wos denied.
        """
        if price+self._balance > self._limit:
            return False
        else:
            self._balance+=price
            return True

    def make_payment(self,amount):
        """Process customer payment that reduces balance（余额）."""
        self._balance-=amount




if __name__ == '__main__':
  wallet = []
  wallet.append(CreditCard('John Bowman', 'California Savings',
                           '5391 0375 9387 5309', 2500) )
  wallet.append(CreditCard('John Bowman', 'California Federal',
                           '3485 0399 3395 1954', 3500) )
  wallet.append(CreditCard('John Bowman', 'California Finance',
                           '5391 0375 9387 5309', 5000) )

  for val in range(1, 17):
    wallet[0].charge(val)
    wallet[1].charge(2*val)
    wallet[2].charge(3*val)

  for c in range(3):
    print('Customer =', wallet[c].get_customer())
    print('Bank =', wallet[c].get_bank())
    print('Account =', wallet[c].get_account())
    print('Limit =', wallet[c].get_limit())
    print('Balance =', wallet[c].get_balance())
    while wallet[c].get_balance() > 100:
      wallet[c].make_payment(100)
      print('New balance =', wallet[c].get_balance())
    print()









