def cleaner(l):

    for x  in l:
        c=l.count(x)
        for i in range(c-1):
            l.remove(x)


    return l
