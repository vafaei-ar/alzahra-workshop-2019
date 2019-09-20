#!/home/gf/packages/anaconda3/bin/python

import os
from sys import argv

add1 = argv[1]
try:
    ch = argv[2]
except:
    ch = ''

def filterfile(add,ch):
    listp = os.listdir(add)
    listo = []
    for i in listp:
        if ch in i:
#            if os.path.isfile(add+'/'+i):
                listo.append(i)
    return listo

list_output = filterfile(add1,ch)
print(list_output)
