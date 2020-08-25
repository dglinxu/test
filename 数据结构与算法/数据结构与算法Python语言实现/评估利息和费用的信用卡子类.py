#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#开发人员：dglin     创建时间：2020/6/7 
#开发工具：PyCharm   文件名称：评估利息和费用的信用卡子类.py   
#E-mail: humen@189.cn
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

class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""

    def __init__(self,customer,bank,acnt ,limit,apr):
        """Create a new predatory credit card instance.

        The initial balance is zero.

        customer  the name of the customer(e.g.,'John Bowman')
        bank      the name of the bank(e.g.,'CAlifornia Savings')
        acnt      the acount identifier (e.g.,5391 0375 93875309')
        limit     credit limit (measured in dollars)
        apr       annual percentage rate(e.g.,0.0825 for 8.25% ARP)
        """

        super().__init__(customer,bank,acnt,limit)
        self._apr=apr

        def charge(self,price):
            """Charge given price to the card,asuming sufficient credit limit.

            Return True if charge was processed.
            Return False and assess $5 fee if charge is denied. 收费被拒，核定5美元服务费
            """
            success=super().charge(price)
            if not success:
                self._balance+=-5
            return success

        def process_month(self):
            """Assess monthly interest on outstanding balance."""

            if self._balance>0:
               # if positive balance,convert APr to monthly multiplicative factor
                monthly_factor=pow(1+self._apr,1/12)
                self._balance*=monthly_factor




