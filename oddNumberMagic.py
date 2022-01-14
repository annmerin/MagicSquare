import math
import numpy as np


def oddnumbermagic(size):
    print(size)
    msquare = np.zeros((int(size), int(size)))
    print(msquare)
    fno = int(size) / 2
    fno = math.floor(fno) # to get the x position of the first number
    # add the first number
    msquare[0,fno] = 1
    # add the second number
    no = 2
    # get the position of number 1 using where key
    index_y,index_x = np.where(msquare == no-1)
    print(index_y,index_x)
    index_y -= 1
    index_x +=1
    print(index_y, index_x)
    if index_y < 0 and index_x <= int(size) - 1:
        index_y = int(size) - 1
        msquare[index_y,index_x] = no
        print(msquare)
        print(index_y, index_x)
        no += 1
        print(no)
        index_y -= 1
        index_x += 1
    elif index_y > 0 and index_x > int(size) - 1:
        index_x = 0
        print(index_y,index_x)
        msquare[index_y,index_x] = no
        no += 1
    else:
        print(index_y, index_x)
        msquare[index_y, index_x] = no
        print(msquare)





