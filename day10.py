import math
import os
import random
import re
import sys
from itertools import groupby


if __name__ == '__main__':
    n = int(input().strip())
    
    binary_value = bin(n)[2:]
    print(list(groupby(binary_value, lambda x:x=="0") ))
    list_1 = [list(group_) for key_, group_ in groupby(binary_value, lambda x:x=="0") if not key_]
    print(list_1)
    lol_ = []
    for list_ in list_1:
        lol_.append(len(list_))
    print(lol_)
    print(max(lol_))
    
         
    
        
        
   
        
