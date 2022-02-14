def pro(k,m,n):
    total = k + m + n
    population = [k, m, n]
    prob_recessive = [0, 0.5, 1] # probability of recessive (a)
    result = 0 # probability of aa
    for i, p in enumerate(population):
        allen_1 = p * prob_recessive[i] / total
        for j, q in enumerate(population):
            if i == j:
                allen_2 = (q - 1) * prob_recessive[j] / (total -1)
            else:
                allen_2 = q * prob_recessive[j] / (total -1)

            result += allen_1 * allen_2
    
    print(1- result) # probability of AA and Aa


pro(17,15,22)