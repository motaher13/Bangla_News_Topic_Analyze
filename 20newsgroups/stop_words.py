# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 11:46:16 2018

@author: Motaher
"""

stop_words = []

# open file and read the content in a list
with open('listfile.txt', 'r',encoding='utf-8') as filehandle:  
    for line in filehandle:
        # remove linebreak which is the last character of the string
        current = line[:-1]

        # add item to the list
        
        stop_words.append(current)

stop_words=set(stop_words)
stop_words=list(stop_words)

        
with open('listfile1.txt', 'a',encoding='utf-8') as the_file:
    for line in stop_words:
        the_file.write(line+'\n')