def file_probas(a,b):
    P=list_prime(a,b)
    R=[]
    F=[]

    for i in range(len(P)-1):
        R.append((P[i+1]-P[i])//2)
        F.append((P[i+1]-P[i])//2)


    univers=cleaner(cleaner(R))

    univers.sort()

    f=open("C:/Users/ahafd/Desktop/contest_paper_2020/probas_reste.txt","w")


    f.write("#############################################\n")
    f.write("Une vision probabiliste des pseudo_restes entre ")
    f.write(str(a))
    f.write(" et ")
    f.write(str(b))
    f.write("\n")
    f.write("#############################################\n")
    f.write("univers=")
    f.write(str(univers))
    f.write("\n")
    for i in range(len(univers)):
        f.write("P(")
        f.write(str(univers[i]))
        f.write(")=")
        f.write(str((F.count(univers[i]))/len(F)))
        f.write("\n")

    f.close()




