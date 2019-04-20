# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 15:29:55 2015

@author: Jason Payne
"""

# Summing (to n) module

def sum_up_to(n):
    msg = "Summing the numbers up to " + str(n) + " = "
    if n == 0:
        msg = msg + "0"
    elif n == 1:
        msg = msg + "1"
    else:
        result = 0
        for i in range(n+1):
            result = result + i
        msg = msg + str(result)
    print(msg)

if __name__ == "__main__":
    import sys
    sum_up_to(int(sys.argv[1]))
