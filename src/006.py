#val = 0
#for i in range(1,11):
#    val += i
#print(val)


#val = 1
#for i in range(1,11):
#    val *= i
#print(val)





import sys
n = int(sys.argv[1])
val = 1

while n > 0:
    val *=n
    n -= 1
print(val)
