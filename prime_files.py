def prime_files(start,step,number_files):
    A=start
    B=A+step
    import time
    s=0
    for i in range(1,number_files+1):
        time_start=time.time()
        name_file=str(A)+"I"+str(B)+".txt"
        f=open(str(name_file),"w")
        f.write("\n##########################\n")
        f.write(" prime numbers between ")
        f.write(str(A))
        f.write(" and ")
        f.write(str(B))
        f.write("\n##########################\n")
        P=list_prime(A,B)
        R=[]
        for i in range(len(P)-1):
            f.write(" the pseudo rest of ")
            f.write(str(P[i+1]))
            f.write(" and ")
            f.write(str(P[i]))
            f.write(" is : ")
            f.write(str((P[i+1]-P[i])//2))
            f.write("\n")

        A=B
        B=A+step
        time_end=time.time()
        f.write("\n")
        f.write("complexite=")
        f.write(str(time_end-time_start))
        f.write("\n")
        f.close()
        s=s+time_end-time_start
        print(time_end-time_start)
    print("complexite total est :",s)









