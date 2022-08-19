import sys
import glob
import os
def is_valid(value: str) -> bool:
    acc = []
    brackets = ('()', '[]', '{}')
    for ch in value:
        for br in brackets:
            if ch == br[0]:
                acc.append(br[0])  
            elif ch == br[1]:
                if not acc or acc[-1] != br[0]:
                    return False  
                acc.pop()
    return len(acc) == 0 
os.chdir(sys.argv[1]) 
for file in glob.glob("*.txt"):
    f=open(file)
    str=f.read()
    print(f"{file} - {is_valid(str)}")
    f.close()