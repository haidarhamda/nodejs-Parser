def cyk(w,Grammar):
    # w = string
    # grammar = dictionary cnf

    n = len(w)
    dp = [[set([]) for i in range(n)] for j in range(n)]

    for i in range(n):
        for nonterm in Grammar.items():
                for term in nonterm[1]:
                    if len(term) == 1 and term[0] == w[i]:
                        dp[i][i].add(nonterm[0])

    for l in range(2,n):
        for i in range (n-l+1):
            j = i+l-1
            for k in range (i,j-1):
                for nonterm in Grammar.items():
                    for prod in nonterm[1] :
                        if len(prod) == 2 :
                            if(prod[0] in dp[i][k]) and (prod[1] in dp[k+1][j]):
                                dp[i][j].add(nonterm[0])
    if "S" in dp[1][n-1] :
        print("Valid")
    else :
        print("gk valid")


