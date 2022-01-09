#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'strmethod' function below.
#
# The function accepts following parameters:
#  1. STRING para
#  2. STRING spch1
#  3. STRING spch2
#  4. LIST li1
#  5. STRING strf
#
from collections import Counter

def stringmethod(para, special1, special2, list1, strfind):
    # Write your code here
    # Write your code here
    #1 -- Remove all special character from para specified in special1 and save them in a variable word1.
    for _ in special1:
        para = para.replace(_,"")
        
    word1 = para
    
    #print(word1)
    #2 get the first 70 charachter from word1, reverse the string, save it in var word2 and print it 
    rword2_tmp1 = word1[:70]
    rword2 = rword2_tmp1[::-1]
    print(rword2)
    
    #3 remove all wide spaces from rword2, join the character using special char specified in special character2 and print the joint string
    joint_string = ''
    x = rword2.replace(" ","")
    for i in x:
        if i != x[-1]:
            joint_string += i + special2
        else:
            joint_string += i

    print(joint_string)
    
    #4 if every string from list1 is present in para, then format the print statement as follows 
    counter = 0
    for lst_tmp in list1:
        che =  len(list1)
        if lst_tmp in para:
            counter += 1 
        else:
            pass
        
    if che == counter:  
        print(f"Every string in {list1} were present")
    else:
        print(f"Every string in {list1} were not present")
      
        
    #5 split every word from word1 and print the first 20 strings as a list
    temp_wrd = word1.split(" ")
    print(temp_wrd[:20])
    
    #6 -- calculate the less frequently used word whose count < 3 and print the last 20 less frequent words as a list Note : count the words as they apprear
    new_var = word1.split(" ")

    counts = Counter(new_var)

    new_lst = list(counts.keys())
    
    if new_lst[-1] == "":
        print(new_lst[-21:-1])
    else:
        print(new_lst[-20:])
    
    #7 print the last index in word1, where the substring strfind is found

    if strfind in word1:
        print(word1.rindex(strfind))

if __name__ == '__main__':
    para = input()

    spch1 = input()

    spch2 = input()
    
    qw1_count = int(input().strip())

    qw1 = []

    for _ in range(qw1_count):
        qw1_item = input()
        qw1.append(qw1_item)

    strf = input()

    stringmethod(para, spch1, spch2, qw1, strf)
