def pseudo_reste(a,b):
    import os
    l=list_prime(a,b)
    R=[]
    f=open("C:/Users/ahafd/Desktop/contest_paper_2020/pseudo_restes.txt","w")
    f.write("#########################\n")
    f.write("les pseudo_restes entre ")
    f.write(str(a))
    f.write(" et ")
    f.write(str(b))
    f.write("\n")
    f.write("#########################\n")
    for i in range(len(l)-1):
        R.append((l[i+1]-l[i])//2)
        f.write(str((l[i+1]-l[i])//2))
        f.write(" entre ")
        f.write(str(l[i+1]))
        f.write(" et ")
        f.write(str(l[i]))
        f.write("\n")
    NEW=[]
    g=open("C:/Users/ahafd/Desktop/contest_paper_2020/MMM.txt","w")
    for i in range(len(R)-1):
        NEW.append(R[i+1]-R[i])
    g.write(str(R))
    g.write("\n")
    g.write(str(NEW))
    g.close()
    print(R)
    return NEW

    f.close()
