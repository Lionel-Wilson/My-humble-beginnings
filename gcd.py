# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 19:25:33 2021

@author: Lione
"""

def gcd(x,y):
    while x!=y:
        print(f"x={x}y={y}")
        if x>y:
            x=x-y
        else:
            y=y-x
    return x