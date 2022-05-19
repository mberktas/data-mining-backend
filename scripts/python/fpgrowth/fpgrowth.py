from collections import defaultdict, OrderedDict
from csv import reader
from email import header
from itertools import chain, combinations
import json
from optparse import OptionParser
from fpgrowth_utils import *


def fpgrowthFromFile(fname, minSupRatio, minConf):
    itemSetList, frequency = getFromFile(fname)
    minSup = len(itemSetList) * minSupRatio
    fpTree, headerTable = constructTree(itemSetList, frequency, minSup)
    if(fpTree == None):
        data = {"datas" : [] , "transaction" : itemSetList.__len__() , "frequentItemSet" : headerTable.__len__()}
        print(json.dumps(data))
        return itemSetList,[],headerTable
    else:
        freqItems = []
        mineTree(headerTable, minSup, set(), freqItems)
        rules = associationRule(freqItems, itemSetList, minConf)
        data = {"datas" : rules , "transaction" : itemSetList.__len__() , "frequentItemSet" : headerTable.__len__()}
        print(json.dumps(data))
        return freqItems, rules,headerTable

if __name__ == "__main__":
    optparser = OptionParser()
    optparser.add_option('-f', '--inputFile',
                         dest='inputFile',
                         help='CSV filename',
                         default="C:/Users/Muhammet/Desktop/node/scripts/python/tesco2.csv")
    optparser.add_option('-s', '--minSupport',
                         dest='minSup',
                         help='Min support (float)',
                         default=0.8,
                         type='float')
    optparser.add_option('-c', '--minConfidence',
                         dest='minConf',
                         help='Min confidence (float)',
                         default=0.3,
                         type='float')

    (options, args) = optparser.parse_args()

    freqItemSet, rules,headerTable = fpgrowthFromFile(
        options.inputFile, options.minSup, options.minConf)

    # print(freqItemSet)
    # print("####################################\n")
    # print(headerTable)
    # print("####################################\n")

    # #data = {"datas" : rules , "transaction" : itemSetList.__len__() , "frequentItemSet" : L1ItemSet.__len__()}

    # print(rules)