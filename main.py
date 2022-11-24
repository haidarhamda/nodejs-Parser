from parser import *
from CFG2CNF import *
from cyk2 import *

c=parseNODEJS("tes.txt")
terminal = getTerminals("terminal.txt")
a,b=parseFACFG(c,terminal)
o=[]
for w in b:
    o.append([w])
print(a)
print(o)
cnf=getCNF("CNF.txt")
p=cyk(o,cnf)
displayMatrix(p)
if(cekcyk(p)):
    print("valid")