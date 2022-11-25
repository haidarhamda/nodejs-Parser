from parserr import *
from CFG2CNF import *
from cyk2 import *
from fa import *
import argparse
from CFG import *
import os
parser = argparse.ArgumentParser(description='open file')
parser.add_argument('file_name',type=str, help='name of file', nargs='?')
args = parser.parse_args()

if __name__=="__main__":
    path=str(args.file_name)
    c=parseNODEJS(path)
    terminal = getTerminals("terminal.txt")
    a,b=parseFACFG(c,terminal)
    o=[]
    for w in b:
        o.append([w])
    # print(a)
    # print(o)
    cnf=getCNF("CNF2.txt")
    p=cyk(o,cnf)
    # displayMatrix(p)
    if(cekcyk(p) and checkOp(a,operationChecker) and checkVar(a,variableChecker)):
        print("Accepted")
    else:
        print("Syntax Error")