#from CFG import getTerminals
import itertools as it

def parseFACFG(parsedArray,CFGterminal):
    arrayCFG = parsedArray.copy()
    tempFA = []
    arrayFA = []

    nonVar = ["1","2","3","4","5","6","7","8","9","0","/","**","*","+","-","%","&","|",'++','--','&&','||','<<','>>','~','!']

    isKurung = False

    stackKurung = []
    index = 0

    for alphabet in parsedArray:
        #print(tempFA)
        if alphabet not in CFGterminal :
            if alphabet == "nl" :
                if any(e in tempFA for e in nonVar):
                    arrayCFG.insert(index,"operation")
                    index += 1
                    arrayCFG.pop(index)
                elif len(tempFA) != 0:
                    arrayCFG.insert(index,"var_name")
                    index += 1
                    arrayCFG.pop(index)
                else :
                    arrayCFG.pop(index)
                tempFA.append(alphabet)
                arrayFA.extend(tempFA.copy())
                tempFA = []
            else :
                tempFA.append(alphabet)
                arrayCFG.pop(index)
        elif len(tempFA) != 0 :
            #print(tempFA)
            if any(e in tempFA for e in nonVar):
                arrayCFG.insert(index,"operation")
            else :
                arrayCFG.insert(index,"var_name")
            
            index += 2
            if alphabet == "(" or alphabet == "=" or alphabet == "return" or alphabet == ";" or alphabet == "." or alphabet == "break" or alphabet == ";" or alphabet == "." or alphabet == ":":
                tempFA.append(":-")
            arrayFA.extend(tempFA.copy())
            tempFA = []
        else :
            if alphabet == "=" or alphabet == "(" or alphabet == "return" or alphabet == ";" or alphabet == "." or alphabet == "break" or alphabet == ":":
                arrayFA.append(":-")
                index += 1
            else :
                index += 1
        #print(arrayCFG)
    #print(arrayFA)
    return arrayFA,arrayCFG

def parseNODEJS(path):
    mustIgnore = False
    with open(path) as file:
        lines = file.readlines()
        terminals = []
        symbols = [';','(', ')','[',']','{','}','++','--','**',':','/','"',"'",',','.','%','==','!','&&','||','<=','>=','>>','<<','!','~','+=','-=',"/=","*=","&=","|="]
        symbols2 = ['=','+','-','*','<','>','&',"|"]
        for line in lines:
            for symbol in symbols:
                line = line.replace(symbol, " "+symbol+" ")
            line = line.split()
            for i,terminal in enumerate(line) :
                for symbol in symbols2 :
                    if terminal not in symbols:
                        terminal = terminal.replace(symbol, " "+symbol+" ")
                    #print(terminal)
                line.pop(i)
                line.insert(i,terminal.split())
            line = list(it.chain.from_iterable(line))
            #print(line)
            #print(line)
            if line[:2] == ["/","/"] :
                line = []
            if line[:2] == ["/","*"] :
                mustIgnore = True
    
            if not mustIgnore:
                line.append("nl")
                terminals.extend(line.copy())
            
            if line[-2:] == ["*","/"] :
                mustIgnore = False

        return terminals

if __name__ == "__main__" :
    from CFG import getTerminals

    c = parseNODEJS("tes.txt")

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