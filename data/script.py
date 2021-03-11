# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 23:39:46 2021

@author: Nikhil Gavin Crasta
"""
import re
import subword_nmt

#FOR french files
file1 = 'EMEA_train.fr'
file2 = 'ep7_train.fr'
file3 = 'EMEA_train.en'
file4 = 'ep7_train.en'

def french_file(file1,file2):
    data = data2 = ''
    with open(file1,'r',encoding="utf8") as f:
        data = f.read()

    with open(file2,'r',encoding="utf8") as g:
        data2 = g.read()
    
    data += '\n'
    data += data2

    with open('train.fr','w',encoding="utf8") as h:
        h.write(data)


#FOR english files
def engfile(file3,file4):
    data = data2 = ''
    with open('EMEA_train.en','r',encoding="utf8") as f:
        data = f.read()

    with open('ep7_train.en','r',encoding="utf8") as g:
        data2 = g.read()
    
    data += '\n'
    data += data2

    with open('train.en','w',encoding="utf8") as h:
        h.write(data)
    
#engfile(file3, file4)
#french_file(file1,file2)
#print(re.sub('[!,*)@#(&$_?.^]',' ',g))