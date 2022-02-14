ls = [1, 1, 1]

def recur(n, k):
    if n < 0:
        return 0
    elif n == len(ls):
        result = recur(n-1, k) + recur(n-2,k) - recur(n-k-1, k)
        ls.append(result)
        return  result
    elif n > len(ls):
        result = recur(n-1, k) + recur(n-2,k) - recur(n-k-1, k)
        return result
    else:
        return ls[n]
    


print(recur(92,18))