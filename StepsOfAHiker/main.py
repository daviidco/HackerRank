#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def createMatrix(size):
    mat = []
    for i in range(size):
        mat.append([])
        for j in range(size):
            mat[i].append(' ')
    return mat


def printMatrix(mat):
    for line in mat:
        print(''.join(map(str, line)))
        
def countingValleys(steps, path):
    # Code to print histogram
    #cadPath = '_'
    #cadPath += ''.join(list(map(lambda x: '/' if x == 'U' else "\\", path)))
    #cadPath += '_'

    #mat_cad = createMatrix(len(cadPath))

    #level_cad = 0

    #for i in range(len(cadPath)):
    #    if cadPath[i] == chr(92):
    #        if cadPath[i-1] in ['_', chr(92)]:
    #            level_cad += 1

    #    elif cadPath[i] == "/" and cadPath[i-1] == "/":
    #        level_cad -= 1
    #    elif cadPath[i] == '_' and cadPath[-i] == '/':
    #        level_cad -= 1

    #    mat_cad[level_cad + len(cadPath)//2][i] = cadPath[i]

    #printMatrix(mat_cad)
    
    # Main code
    # Write your code here
    l = path.strip().lower()
    valleys = 0
    level = 0
    for i in range(len(l)):
        if level == 0 and l[i] == 'd':
            for k in range(i+1, len(l)):
                if level == 0 and l[k] == 'u':
                    valleys += 1
                    break

                elif l[k] == 'u':
                    level += 1
                elif l[k] == 'd':
                    level -= 1
                    print("incompleted valley")

        if l[i] == 'u':
            level += 1
        else:
            level -= 1


    print("# Valleys:", valleys)
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
