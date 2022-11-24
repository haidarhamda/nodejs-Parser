from CFG import getTerminals

def parseFACFG(parsedArray,CFGterminal):
    arrayCFG = parsedArray.copy()
    tempFA = []
    arrayFA = []

    nonVar = ["1","2","3","4","5","6","7","8","9","0","/","**","*","+","-","%"]

    isKurung = False

    stackKurung = []
    index = 0

    for alphabet in parsedArray:
        if alphabet not in CFGterminal :
            tempFA.append(alphabet)
            arrayCFG.pop(index)
        elif len(tempFA) != 0 :
            if alphabet == "(" or alphabet == "=":
                tempFA.append(":-")
            if any(e in tempFA for e in nonVar):
                arrayCFG.insert(index,"operation")
            else :
                arrayCFG.insert(index,"var_name")
            index += 2
            arrayFA.extend(tempFA.copy())
            tempFA = []
        else :
            if alphabet == "=":
                tempFA.append(":-")
                index += 2
            else :
                index += 1
    return arrayFA,arrayCFG

def parseNODEJS(path):
    mustIgnore = False
    with open(path) as file:
        lines = file.readlines()
        terminals = []
        symbols = ['(', ')','[',']','{','}','+','-','*',':','/', '>','<' ,'"',"'",',','.','%','=','!','#']
        for line in lines:
            for symbol in symbols:
                line = line.replace(symbol, " "+symbol+" ")
            line = line.split()
            #print(line)
            if line[:2] == ["/","/"] :
                line = []
            if line[:2] == ["/","*"] :
                mustIgnore = True

            if not mustIgnore:
                terminals.extend(line.copy())
            
            if line[-2:] == ["*","/"] :
                mustIgnore = False

        return terminals

if __name__ == "__main__" :
    c = parseNODEJS("nodejs.txt")

    print(c)
    terminal = getTerminals("terminal.txt")
    p = ["(","a","+","b",")","if","if","(","(","a","if","b",")",")",")","{","a","+","b","}","{","a","anjing","\""]
    a,b = parseFACFG(c,terminal)


    print(b)
    # a = []
    # a.extend(p)
    # a.extend(p.copy())

    print(a)
    #print(b)