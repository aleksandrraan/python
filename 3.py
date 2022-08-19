count=int(input())
k=0
c=1
for i in range (0,count+1):
    c+=i
for i in range (0,count+1):
    print(count*" ",end=" ")
    for k in range (c-1,c-i-1,-1):
        print(k,end=" ")
    c-=i
    count-=1
    print()

