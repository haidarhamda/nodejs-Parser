from CFG import getTerminals

def parseFACFG(parsedArray,CFGterminal):
    arrayCFG = parsedArray.copy()
    tempFA = []
    arrayFA = []

    isKurung = False

    stackKurung = []
    index = 0

    for alphabet in parsedArray:
        if isKurung :
            if alphabet not in CFGterminal :
                tempFA.append(alphabet)
                arrayCFG.pop(index)
            elif alphabet == "(" :
                tempFA.append(alphabet)
                arrayCFG.pop(index)
                stackKurung.append(alphabet)
            elif alphabet == ")" :
                if len(tempFA) != 0 and len(stackKurung) == 0:
                    arrayCFG.insert(index,"operation")
                    index += 2
                    arrayFA.extend(tempFA.copy())
                    tempFA = []
                    isKurung = False
                elif len(stackKurung) == 0:
                    index += 1
                    isKurung = False
                else :
                    tempFA.append(alphabet)
                    arrayCFG.pop(index)
                    stackKurung.pop(0)
            elif len(tempFA) != 0 :
                arrayCFG.insert(index,"operation")
                index += 2
                arrayFA.extend(tempFA.copy())
                tempFA = []
            else :
                index += 1
        elif alphabet not in CFGterminal :
            tempFA.append(alphabet)
            arrayCFG.pop(index)
        elif len(tempFA) != 0 :
            if alphabet == "(" :
                isKurung = True
            arrayCFG.insert(index,"operation")
            index += 2
            arrayFA.extend(tempFA.copy())
            tempFA = []
        else :
            if alphabet == "(" :
                isKurung = True
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