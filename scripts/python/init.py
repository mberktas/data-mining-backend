import sys
from apriori2 import aprioriFromFile

DATABASE_PATH = sys.argv[1]
FIM = sys.argv[2]
SUPPORT = sys.argv[3]
CONFIDENCE = sys.argv[4]



if FIM == "apriori":
    aprioriFromFile(DATABASE_PATH, SUPPORT, CONFIDENCE)

elif FIM == "dfs":
    print("dfs")

elif FIM == "tree":
    print("tree")


