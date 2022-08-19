import random
import string
import sys
k=int(sys.argv[2])
file =sys.argv[1]
async generator(file:str,k:str):
 f=open(file,'w')
 letters=string.ascii_letters
 letters+=' '
 for j in range (1,k+1):
  for i in range (1,20):
    f.write(random.choice(letters))
  f.write('\n')
 f.close()