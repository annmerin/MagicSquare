import math
import numpy as np


def oddnumbermagic(size):
    msquare = np.zeros((int(size), int(size)))
    max = int(size)*int(size)
    fno = int(size) / 2
    fno = math.floor(fno) # to get the x position of the first number
    # add the first number
    msquare[0,fno] = 1
    max -= 1
    # add the second number
    no = 2
    # get the position of number 1 using where key
    index_y,index_x = np.where(msquare == no-1)
    index_y -= 1
    index_x +=1
    while max >= 1 :
        if index_y < 0 and index_x > 0 and index_x < int(size) :
            index_y = int(size) - 1
            msquare[index_y,index_x] = no
            no += 1
            index_y -= 1
            index_x += 1
            max -= 1
            if max == 0:
                break
        if (index_y > 0 and index_y < int(size)) and index_x >= int(size) :
            index_x = 0
            msquare[index_y,index_x] = no
            no += 1
            max -= 1
            index_y -= 1
            index_x += 1
            if max == 0:
                break
        if (index_y >= 0 and index_y < int(size)) and (index_x >= 0 and  index_x < int(size)) and msquare[index_y, index_x] == 0:
            msquare[index_y, index_x] = no
            no += 1
            max -= 1
            index_y -= 1
            index_x += 1
            if max == 0:
                break
        if (index_y >= 0 and index_y < int(size)) and (index_x >= 0 and  index_x < int(size)) and msquare[index_y, index_x] != 0:
            index_y +=2
            index_x -=1
            msquare[index_y, index_x] = no
            no += 1
            max -= 1
            index_y -= 1
            index_x += 1
            if max == 0:
                break
        if (index_y >= 0 and index_y < int(size)) and index_x >= int(size) :
            index_x = 0
            msquare[index_y, index_x] = no
            no += 1
            index_y -= 1
            index_x += 1
            max -= 1
            if max == 0:
                break
        if index_y < 0 and index_x >= int(size) :
            index_y += 2
            index_x -= 1
            msquare[index_y,index_x] = no
            no += 1
            index_y -= 1
            index_x += 1
            max -= 1
            if max == 0:
                break
    print(msquare)









