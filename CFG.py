import os


def getCFG(path):
    f = open(path)
    lines = f.readlines()
    f.close()
    cfg=[]
    for line in lines:
        if ' -> ' in line:
            line =line.replace(' -> ',' ').replace('\n','')
            line = line.split(' ')
            productions = [line[0]]
            # if '|' in line:
            for i in range (1,len(line)):
                # print(productions)
                if line[i]=='|':
                    cfg.append(productions)
                    productions=[line[0]]
                else:
                    productions.append(line[i])
                # cfg.append(productions)
                if i==len(line)-1:
                    cfg.append(productions)
            # else:
            #     cfg.append(productions.append(line))
        # cfg.append(productions)


        # line =line.replace('\n','')

        # print(line)
        # cfg.append(line.split(' '))

        # print(line)
        # print(cfg)
    return  cfg
def getTerminals(path):
    f =open(path)
    lines=f.readlines()
    f.close()
    terminal=[]
    for line in lines:
        if not (line.startswith("\n")):
            line = line.replace("\n","")
            terminal.append(line)
    return terminal

#  Membuat rule terminal
def getProdRules(path):
    terminals = getTerminals(path)
    ProdRules = []
    for terminal in terminals:
        rule = terminal.upper() + "_rule" # Membuat LHS
        ProdRules.append([rule, terminal]) # Membuat prod rule
    return ProdRules

if __name__ == "__main__" :
    cfg = getCFG("CFG2.txt")
    for y in cfg:
        print(y)
    terminal = getTerminals("terminal.txt")
    for y in terminal:
        print(y)
