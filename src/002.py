

#def greet():
#    print("Hello, Bioinformatics")


#def greet1(name: str) -> None:
#    print(f"Hello, {name}")


#def greet2(num: int) -> int:
#    return num * 2

#greet()
#ret1= greet1("glroy")
#print(ret1)

#ret2 = greet2(3)
#print(ret2)


#greet()

#greet1("glory")
#------------------------------------------------
#!/usr/bin/python3

import math
import sys

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [num]")
    sys.exit()

r = int(sys.argv[1])
pi = math.pi
result = round(r**2 * pi, 2)

print(result)

 
 




