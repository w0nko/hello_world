#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 21:38:52 2017

@author: wonko
"""

end = input("Enter a number: ")
#int(end)
#print int(end)
i = 1
while True:
   if (i > 0) and (i <= int(end)):
       temp = i
       i += 1
       temp = temp + i
   print (temp)
    