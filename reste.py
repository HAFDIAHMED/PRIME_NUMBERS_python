def pseudo_reste(A,B):
    L=list_prime(A,B)
    R=[]
    for i in range(len(L)-1):
        R.append((L[i+1]-L[i])//2)
    return R