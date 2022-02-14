
def fac(x):
    if x == 1 or x == 0:
        return 1
    return fac(x-1)*x
    
def permunation(k):
    if k == 1:
        return [['1']]
    
    pre_list = permunation(k - 1)

    ls = []
    for item in pre_list:
        new_item = item.copy()
        new_item.append(str(k))
        ls.append(new_item)
        for i in range(0,len(item)):
            cp_item = item.copy()
            cp_item.insert(i, str(k))
            ls.append(cp_item)
    return ls



def PERM(k):
    total = fac(k)
    print(total)

    result = permunation(k)
    for row in result:
        print(' '.join(row))

PERM(5)