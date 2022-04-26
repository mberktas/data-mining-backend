import sys
import numpy as np

DATABASE  = np.array([['I1','I2','I5'],['I2','I4'],['I2','I3'],['I1','I2','I4'],['I1','I3'],['I2','I3'],['I1','I3'],['I1','I2','I3','I5'],['I1','I2','I3']] , dtype=object,)

MIN_SUPP  = 0.5
MIN_CONF = 0.6


ITEMS = []
ITEMS_COUNT=[]
ITEMSETS = []

def aprior():
    print(DATABASE.shape[0])

    for k in range(0,DATABASE.shape[0]):
        print(DATABASE[k][0])
        for j in range(0, DATABASE.shape[0]):
           break
        

def getItemMinSupp(item):
    itemCount = 0
    str1 = ""
    str2 = ""
    print(str1.join(DATABASE[0]) == str2.join(item))
    for k in range(0, DATABASE.shape[0]):
        print(DATABASE[k])
        if(DATABASE[k].__contains__(item)):
            itemCount += 1
    
    print(itemCount)

def itemSet():
    ITEMSETS =  np.concatenate(DATABASE)    
    ITEMS  = np.unique(ITEMSETS)
    ITEMS_COUNT = np.zeros(len(ITEMS) , dtype= int)
    for k in range(0 , len(ITEMS)):
        for j in range(0 , len(ITEMSETS)):
            if(ITEMS[k] == ITEMSETS[j]):
                ITEMS_COUNT[k] += 1


    
                    
itemSet()
getItemMinSupp(["I1",  "I2" , "I5"])