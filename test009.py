import random
import os
'''产生100个随机数'''
with open('data.txt','w') as fp1:
    for i in range(99):
        fp1.write(str(random.randint(1,1000)))
        fp1.write(',')
    fp1.write(str(random.randint(1, 1000)))
with open('data.txt','r') as fp11:
    txt = fp11.read()
    L = txt.split(',')
with open('data_asc.txt','w+') as fp2:
    L = [int(i) for i in L]
    L.sort()
    L = [str(i) for i in L]
    fp2.write(','.join(L))



