def make_kmer(l1, l2, num):
    if num == 1:
        return l2
    
    tmp= list()
    for e1 in l1:
        for e2 in l2:
            tmp.append(e1+e2)
    return make_kmer(l1,tmp,n-1)


    n=int(sys.argv[1])
    l1= ['A','C','G','T']
    l2= ['A','C','G','T']
    res= make_kmer(l1,l2,n)
    print(res)
    