

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
    tab=[["" for i in range (l)] for i in range (l)]
    for i in range (l):
        tab[i][i]=getState([listword[i]],cnf)
    # displayMatrix(tab)
    for le in range (1,l+1):
        for i in range (l-le+1):
            j=i+le-1
            for k in range (i,j):
                tab[i][j]=getState([tab[i][k],tab[k+1][j]],cnf)
    return tab

def getState(wordlist,cnf):
    print(wordlist)
    for c in cnf:
        # print(len(c))
        # print(len(wordlist))
        if (len(wordlist)==len(c)-1):
            isril = True
            # for i in range (1,len(c)):
            #     # isril=False
            #     if (wordlist[i]==c[i]):
            #         isril=True
            #     else:
            #         isril=False
            #         break
                    # return c[0]
            i=0
            # print(wordlist[i])
            while (isril and i<len(wordlist)):
                # print(wordlist[i])
                # print(c[i])
                if (wordlist[i]!=c[i+1]):
                    isril=False
                i+=1
            if isril:
                return c[0]
        # print(c)
    return "NOTFOUND"

def cekGrammar(wordlist,cnf):
    for c in cnf:
        # print(len(c))
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
                # print(c[i])
                if (wordlist[i] != c[i + 1]):
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
cnf=getCNF("CNF2.txt")
# for c in cnf:
#     print(c)
x="for i in range"
x=x.split(" ")
print(x)
c=[["S","A","B"],["S","S","B"],["A","a"],["B","b"],["B","B","B"]]
print("aa")
print(getState([")"],cnf))
print("bb")
def displayMatrix (matrix):
    for i in range (len(matrix)):
        for j in range (len(matrix[0])):
            if(matrix[i][j]==""):
                print("p",end=" ")
            else:
                print(matrix[i][j], end= " ")
        print()
# print(cyk(x,cnf))
displayMatrix(cyk(["a","b","b","b"],c))
