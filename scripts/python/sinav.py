# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 15:15:56 2021

@author: alive
"""
from itertools import combinations 
import numpy as np

# =============================================================================
# from pytictoc import TicToc
# =============================================================================
database=np.array([[1,1,0,0,1,0,1],
                   [0,1,1,0,1,1,0],
                   [1,0,0,0,1,1,0],
                   [0,1,0,0,0,1,1],
                   [1,1,0,1,1,0,0],
                   [1,0,0,0,0,1,1],
                   [1,1,0,1,1,1,1],
                   [1,1,0,0,1,1,0],
                   [0,1,1,1,0,1,0],
                   [1,0,0,0,1,1,1],
                   [0,1,0,1,1,1,0],])
Gloabalfk=[]
fk=[]
supports=[]
minsup=4
numofitems=database.shape[1]
SingleItems =np.array(["A","B","C","D","E","F","G"])
def DoesExist(itm,transcation):
    if sum(transcation[itm])==len(itm):
        E=1
    else:
        E=0
    return E
# =============================================================================
def Abssupcal(itm,database):
    Absup=0
    for i in range(0,database.shape[0]):
        transcation=database[i,:]
        if DoesExist(itm,transcation):
            Absup+=1
    return Absup
# =============================================================================
def Candidategeneration(fkm1):
    ck=[]
    for i in range(0,len(fkm1)-1):
        for j in range(i+1,len(fkm1)):
            itemset1=fkm1[i]
            itemset2=fkm1[j]
            if all(itemset1[1:]==itemset2[:-1]):
                newitem=np.hstack((np.array(itemset1),np.array(itemset2[-1])))
                ck.append(newitem)
    return ck
# =============================================================================
def Showdatabase(database,SingleItems):
    for i in range(0,database.shape[0]):
        tr=database[i,:]
        I=np.nonzero(tr>0)[0]
        itemset=''
        for itm in SingleItems[I]:
            itemset = itemset + str(itm)
        print(i,': ',itemset)
    return  
# =============================================================================
def FindIndex(itemset, frequentItemsets):
    I = []
    for k in range(0,len(frequentItemsets)):
        tmp = frequentItemsets[k]
        if tmp.shape[0] == itemset.shape[0]:
            if all(itemset == tmp):
                I = k
                break
    return I
 
k=1
for i in range(0,numofitems):
    itm=np.array([i])
    Abssup=Abssupcal(itm,database)
    if Abssup>=minsup:
        fk.append(itm)
        Gloabalfk.append(itm)
        supports.append(Abssup)
        print('Fklar',': ',SingleItems[Gloabalfk[-1]],'Supp.:',Abssup)#fk
# =============================================================================

k=2
loop=1
while loop:
    fkm1=fk; fk=[]
    Ck=Candidategeneration(fkm1)
    for i in range(0,len(Ck)):
        adayogeseti=Ck[i]
        Abssupp=Abssupcal(adayogeseti,database)
        if Abssupp>=minsup:
            fk.append(adayogeseti)
            Gloabalfk.append(adayogeseti)
            supports.append(Abssupp)
            print('Fklar',': ',SingleItems[Gloabalfk[-1]],'Supp.:',Abssupp)#fk
    k+=1
    if len(Ck)*len(fk)==0:
        loop=0

MinCof = 0.90
MinKulc = 0.60
for itemset in Gloabalfk:
    L = itemset.shape[0]
    if 1<L:
        I=FindIndex(itemset,Gloabalfk)
        Supportitemset=supports[I]
        for j in range(1,L):
            CMBN= list(combinations(np.arange(0,L),j))
            CMBN= np.matrix(CMBN)
            for k in range(0,len(CMBN)):
                PrefixIndex= np.array(CMBN[k,:])[0]
                tmp=np.arange(1,L+1)
                tmp[PrefixIndex]=0
                SuffixIndex=np.nonzero(tmp!=0)[0]
                Prefix=itemset[PrefixIndex]
                Suffix=itemset[SuffixIndex]
                
                tmpPrefix=''
                for kk in range(0,np.size(Prefix)):
                    tmpPrefix=tmpPrefix+SingleItems[Prefix[kk]]
                   
              
                tmpSuffix=''
                for kk in range(0,np.size(Suffix)):
                    tmpSuffix=tmpSuffix+SingleItems[Suffix[kk]]
             
                I=FindIndex(Prefix,Gloabalfk)
                Supportprefix=supports[I]
                Confidence=Supportitemset/Supportprefix
              
                I=FindIndex(Suffix,Gloabalfk)
                Supportsuffix=supports[I]
                 
                Kulc=abs(Supportitemset-Supportprefix*Supportsuffix)
                Kulc=0.5*(Supportitemset/Supportprefix+Supportitemset/Supportsuffix)
                #Kulc = abs(Kulc-0.5)*2
                mdfKulc = (Kulc - 0.5)*2
                if MinKulc<=Kulc:
                    if MinCof<=Confidence:
                        print(tmpPrefix,'-->',tmpSuffix,'conf.:',Confidence,"Kulc:",mdfKulc)
                     
                 
# =============================================================================
