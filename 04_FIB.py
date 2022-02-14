
def recur(n, k):
    if n == 1:
        return 1
    if n == 2:
        return 1
    
    return recur(n-1, k) + k * recur(n-2,k)

print(recur(32,2))