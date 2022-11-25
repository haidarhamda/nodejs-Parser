import itertools as it
import parserr as parser

operationChecker = { "q0" : [[["qz"],"/","**","*","+","-","%","&","|",'&&','||','<<','>>','~','!',"==","<=",">=","+=","-=","*=","/="],[["q0"],":-"],[["q3"],'++','--'],[["q4"],"num"],[["q1"]]],
                    "q1" : [[["q2"],"/","**","*","+","-","%","&","|",'&&','||','<<','>>','~','!',"==","<=",">=","+=","-=","*=","/="],[["q0"],":-"],[["q0"],'++','--'],[["qz"]]],
                    "q2" : [[["qz"],":-","/","**","*","+","-","%","&","|",'&&','||','<<','>>','~','!',"==","<=",">=","+=","-=","*=","/=",'++','--'],[["q1"]]],
                    "q3" : [[["qz"],":-","/","**","*","+","-","%","&","|",'&&','||','<<','>>','~','!',"==","<=",">=","+=","-=","*=","/="],[["qz"],"num"],[["q1"]]],
                    "q4" : [[["q2"],"/","**","*","+","-","%","&","|",'&&','||','<<','>>','~','!',"==","<=",">=","+=","-=","*=","/="],[["q0"],":-"],[["qz"]]],
                    "qz" : [[["qz"]]],
                    "deathstate" : ["qz","q3"]}

def checkFA(arrayFA,stateTransition) :
    currentState = "q0"
    for alphabet in arrayFA:
        found = False
        for deltas in stateTransition[currentState]:
            if alphabet in deltas: 
                currentState = deltas[0][0]
                found = True
        if not found :
            currentState = stateTransition[currentState][-1][0][0]
        #print(alphabet)
        #print(currentState)
    if currentState in stateTransition["deathstate"] :
        return False
    return True

def checkOp(arrayFA,stateTransition):
    for i,alphabet in enumerate(arrayFA):
        if alphabet[0] in ['1','2','3','4','5','6','7','8','9','0'] :
            arrayFA.pop(i)
            arrayFA.insert(i,"num")

    return checkFA(arrayFA,stateTransition)

if __name__ == "__main__" :
    from CFG import getTerminals

    c = parser.parseNODEJS("tes.txt")

    #print(c)
    terminal = getTerminals("terminal.txt")
    p = ["(","a","+","b",")","if","if","(","(","a","if","b",")",")",")","{","a","+","b","}","{","a","anjing","\""]
    a,b = parser.parseFACFG(c,terminal)


    print(a)
    print(checkOp(a,operationChecker))
