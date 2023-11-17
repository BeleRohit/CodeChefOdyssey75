"""
Chef aims to be the richest person in Chefland by his new restaurant franchise. Currently, his assets are worth A billion dollars and have no liabilities. He aims to increase his assets by 

X billion dollars per year.

Also, all the richest people in Chefland are not planning to grow and maintain their current worth.

To be the richest person in Chefland, he needs to be worth at least 
�
B billion dollars. How many years will it take Chef to reach his goal if his value increases by 
�
X billion dollars each year?
"""
import math
t=int(input())
for i in range(t):
    a,b,x=map(int,input().split())
    print(math.ceil((b-a)/x))

