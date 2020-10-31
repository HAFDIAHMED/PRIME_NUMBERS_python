def generating(rang):
    import time
    start=time.time()
    born=searching_intervall(rang)
    R=[0]
    R=R+pseudo_reste(0,born)
    prime_rang=3
    for i in range(1,rang+1):
        prime_rang=prime_rang+2*R[i]

    print("prime_rang=",prime_rang)
    stop=time.time()
    print("complexite=",stop-start)
