def list_prime(a,b):
    l=[]
    for i in range(a,b+1):
        if prime(i):
            l.append(i)
    return l