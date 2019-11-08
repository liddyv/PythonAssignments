# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 10:43:19 2019
Assignment 1: how many 20, 10, 5, 1 dollar bills user have in their pocket. 
My bonus point: Calculate the number of total coins in quarter, dime, nickel and penny
@author: WanLing (Liddy) Hsieh
"""

# Calculate dollar bills
twenty = 20
ten = 10
five = 5
one = 1
twenty_bill = 0
ten_bill = 0
five_bill = 0
one_bill = 0

total = input("Please type in total amount (in dollars): ")
total = int(total)

if total >=20:
    twenty_bill = total // twenty
    total %=twenty
if total >=10:
    ten_bill = total // ten
    total %= ten
if total >=5:
    five_bill = total // five
    total %= five
if total > 0:
    one_bill = total // one
    total = 0
print ("Your pocket has %i twenty dollar bills, %i ten dollar bills, %i five dollar bills, and %i one dollar bills" 
       %(twenty_bill, ten_bill, five_bill, one_bill))
    
# Calculate coins
penny = 1
nickel = 5
dime = 10
quarter = 25
p_coin=0
n_coin=0
d_coin=0
q_coin=0

cents = input("Please enter an amount no more than 1 dollar(in cents): ")
cents = int(cents)
if cents >=25:
    q_coin = cents/quarter
    cents %= quarter
if cents >=10:
    d_coin = cents/dime
    cents %= dime
if cents >=5:
    n_coin = cents/nickel
    cents %= nickel    
if cents > 0:
    p_coin = cents/penny
    cents = 0

print ( "The coins are %i quarters, %i dimes, %i nickels and %i pennys." %(q_coin,d_coin,n_coin,p_coin) )
   