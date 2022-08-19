import random
r=random.randint(0,100)
for i in range(1,9):
    k=int(input())
    if r>k:
        print("Не угадал число больше")
    if r<k:
        print("Не угадал число меньше")
    if r==k:
        print("Угадал")
        break
   
   