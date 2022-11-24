import grammpy as gr
# from grammpy import cyk

def getCNF(path):
    f = open(path)
    lines = f.readlines()
    f.close()
    cnf = []
    for line in lines:
        if ' -> ' in line:
            line = line.replace(' -> ', ' ').replace('\n', '')
            line = line.split(' ')
            cnf.append(line)
            # productions = [line[0]]
    return cnf

def cyk(listword,cnf):
    l=len(listword)
    tab=[[[] for i in range (l)] for i in range (l)]
    for i in range (l):
        tab[i][i]=getState([listword[i]],cnf)

    for le in range (1,l+1):
        for i in range (l-le+1):
            j=i+le-1
            for k in range (i,j):
                st=stateTosearch([tab[i][k],tab[k+1][j]])
                # print(f"st:{st},tab[i][k]:{tab[i][k]},tab[k+1][j]:{tab[k+1][j]}")
                tab[i][j]+=getState(st,cnf)
                tab[i][j]=removeDuplicate(tab[i][j])
                # print(k)
                # displayMatrix(tab)
    return tab

def stateTosearch(statelist):
    # print(statelist)
    a=[]
    for i in range(len(statelist[0])):
        for j in range (len(statelist[1])):
            a.append([statelist[0][i],statelist[1][j]])
    # print(a)
    return a
def removeDuplicate(x):
  return list(dict.fromkeys(x))
def getState(wordlist,cnf):
    # print(wordlist)
    a=[]
    # print(cnf)
    for c in cnf:
        # print(c)
        for j in range (len(wordlist)):
            if (len(wordlist[j])==len(c)-1):
                isril = True
                i=0
                # print(wordlist[i])
                # print(c)
                while (isril and i<len(wordlist[j])):
                    if (wordlist[j][i] not in c[i+1]):
                        isril=False
                    # print(i)
                    i+=1
                if isril:
                    a.append(c[0])
        # print(c)
    return a

def cekGrammar(wordlist,cnf):
    print(cnf)
    for c in cnf:
        print(c)
        print(len(c))
        # print(len(wordlist))
        if (len(wordlist) == len(c) - 1):
            isril = True
            # for i in range (1,len(c)):
            #     # isril=False
            #     if (wordlist[i]==c[i]):
            #         isril=True
            #     else:
            #         isril=False
            #         break
            # return c[0]
            i = 0
            # print(wordlist[i])
            while (isril and i < len(wordlist)):
                # print(wordlist[i])
                print(c[i])
                if (wordlist[i] not in c[i + 1]):
                    isril = False
                i += 1
            if isril:
                return True
        # print(c)
    return False
# def cekGrammar(word,cnf,state):
#     for c in cnf:
#         if (state==c[0]):
#             if (word==c[1]):
#                 return True
#     return False
if __name__ == "__main__" :
    cnf=getCNF("CNF.txt")
    # print(cnf)
    # print(cnf)
    # for c in cnf:
    #     print(c)
    x="for i in range"
    x=x.split(" ")
    print(x)
    c=[["S","A","B"],["S","B","C"],["A","a"],["A","B","A"],["B","C","C"],["B","b"],["C","A","B"],["C","a"]]
    # print("aa")
    # print(getState([")"],cnf))
    # print("bb")
    def displayMatrix (matrix):
        for i in range (len(matrix)):
            for j in range (len(matrix[0])):
                if(matrix[i][j]==""):
                    print("p",end=" ")
                else:
                    print(matrix[i][j], end= " ")
            print()
    # print(cyk(x,cnf))
    # displayMatrix(cyk(["a","a","b","a","b"],c))
    displayMatrix(cyk([["if"],["("],["operation"],[")"],["{"],["operation"],["}"]], cnf))

    # print(stateTosearch([["S","A"],["A","C"]]))
    # o=cyk(c,["b","a","a","b","a"])
    # print(o)