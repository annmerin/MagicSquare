import math
import numpy as np


def oddnumbermagic(n):
    print(n)
    msquare = np.zeros((int(n), int(n)))
    print(msquare)
    fno = int(n) / 2
    fno = math.floor(fno)
    print(fno)
    # add the first number
    msquare[0,fno] = 1
    print(msquare)
    fno+=1
    print(fno)
    # add the second number
