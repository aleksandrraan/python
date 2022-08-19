import random
import pif
from re import I

a=random.randint(1,10)

b=0
for i in range(1,4):
    print(f"popitka {i}")
    b=int(input())
    if a==b:
        print("Ura")
        break    
