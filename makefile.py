def make_file():
    for i in range(1,3):
        s="name"+str(i)+".txt"
        print(s)
        f=open(str(s),"w")
        f.write("test")
        f.write(str(i))
        f.close()
