def probas(a,b,x):
    P=list_prime(a,b)
    R=[]
    for i in range(len(P)-1):
        R.append((P[i+1]-P[i])//2)
    #print("P(",x,")=",(R.count(x))/len(R))
    return (R.count(x))/len(R)