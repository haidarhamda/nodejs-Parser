import CFG as Cfg

# menghapus unit production dari CFG
def removeProd(cfg, terminals):
    delete = []
    for prod in cfg:
        if ((len(prod) == 2) and (not(prod[1] in terminals))):
            if (prod[1] == prod[0]): 
                continue # mengabaikan S -> S
            else: #(prod[1] != prod[0]): 
                i = 0
                while(i < len(cfg)):
                    if (prod[1] == cfg[i][0]):
                        temp = [prod[0]]
                        for j in range(1, len(cfg[i])):
                            temp.append(cfg[i][j])
                        cfg.append(temp)   
                    i += 1
            delete.append(prod)
    for prod in delete:
        cfg.remove(prod)
    return cfg

def getRule(terminal, rules):
    # Mengecek apakah terminal sesuai dengan daftar terminal
    for rule in rules:

        if (rule[1] == terminal):
            return rule[0]

def checkRHS(cfg, terminals, rules):
    # Mengecek isi dari RHS apakah sudah sesuai dengan syarat CNF 
    for prod in cfg:
        # Mengecek apakah terdapat lebih dari 1 terminal di RHS
        if (len(prod) > 2):
            if any(elmt in prod for elmt in terminals):
                for i in range(len(prod)):
                    if (prod[i] in terminals):
                        prod[i] = getRule(prod[i], rules) # convert term to its corresponding non-term
    count = 1
    idx = 1
    for prod in cfg:
        # Mengecek apakah terdapat lebih dari 2 non terminal di RHS 
        if (len(prod) > 3):
            rule = []
            for i in range(2, len(prod)):
                rule.append(prod[i])
            for i in range(2, len(prod)):
                prod.pop()
            new_variable = rule[0] + "_rule"
            for elmts in cfg:
                if (new_variable in elmts[0]):
                    new_variable += str(count) 
                    break
            prod.append(new_variable)
            rule.insert(0, new_variable)
            if rule not in cfg:
                cfg.insert(idx, rule)  
        idx += 1    
    return cfg


def writeCNF(filecfg, filecnf):
# menulis hasil convert cfg ke cnf ke dalam file txt
    file = open(filecnf, 'w')
    cfg = Cfg.getCFG(filecfg)
    terminals = Cfg.getTerminals("terminal.txt")
    rules = Cfg.getProdRules("terminal.txt")
    cfg = removeProd(cfg, terminals)
    for rule in rules:
        cfg.append(rule)
    cfg = checkRHS(cfg, terminals, rules)
    for rule in rules:
        cfg.remove(rule)
    for prod in rules:
        str = (' -> '.join(prod))
        file.write(str + "\n")
    for prod in cfg:
        str = (' '.join(prod)).replace(' ', ' -> ', 1)
        file.write(str + "\n")
    file.close()

#writeCNF("CFG2.txt","CNF.txt")
