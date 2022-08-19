count=int(input())
k=0
c=1
for i in range (0,count+1):
    for k in range(c,c+i):
        print(k,end=" ")

    print()
    c+=i
