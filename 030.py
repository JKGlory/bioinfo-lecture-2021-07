seq = "AGTTTATAG"


for i in range(len(seq)):
    s = seq[i:i+2]
    print(i, s, s=="TT")

#    if s == "TT":
#        pirnt(i) 



#seq.index("TT")  #겹치는 부분에서는 사용하기가 어렵다.

