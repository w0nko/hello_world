# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

varA = input("Enter input A: ")
varB = input("Enter input B: ")
if type(varA) == str or type(varB) == str:
    print ("string involved")
elif (type(varA) and type (varB)) == int:
    if varA > varB:
        print ("bigger")
    elif varA == varB:
        print ("equal")
    else:
        print ("smaller")