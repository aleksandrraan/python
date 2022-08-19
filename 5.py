import random
from tkinter import W
c=int(input())
f=open("alex.txt","w")
for i in range (1,9):
    k=random.randint(1,100)
    if k==c:
        f.write("=")
        break
    if k>c:
        f.write("-")
    if k<c:
        f.write("+")
    
f.close()