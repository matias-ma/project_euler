#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11

import numpy as np 

rep = 60

def len_path(n):
    i = 0
    steps = 0
    q = 2
    while i < 1:
        if q == 2 and steps >= 1:
            i += 1
        elif q <= n/2:
            q = 2*q - 1
            steps += 1
        elif q > n/2:
            q = 2*q - n
            steps += 1
        elif steps > rep:
            break
    return steps

d = 0
i=0
all_n = np.array([])
while d <= 2**rep:
    d += 2
    if len_path(d) == rep:
        all_n = np.append(d, all_n)
        print(all_n)
        print(sum(all_n))
        
