import sys

##설명서
if len(sys.argv) != 2:
    print(f"python {sys.argv[0]} [sample]")
    sys.exit(1)




sample = sys.argv[1]
print(f"processing: {sample}")
##처리 분석
print(f"end: {sample}")


---------------------------------------------
if len(sys.argv) != 2:
    print(f"python {sys.argv[0]} [num]")
    sys.exit(1)

#num = int(sys.argv[1])
try:
    res = 10 / num
except ZeroDivisionError:
    sys.exit(2)
print(res)


-------------------------------------
if len(sys.argv) != 2:

    print(f"python {sys.argv[0]} [num]")
    sys.exit(1)

#num = int(sys.argv[1])

try:
    num = int(sys.argv[1])
except ValueError as err:
    print(f"{err}, your input: {sys.argv[1]}")
    sys.exit(3)
try:
    res = 10 / num
except ZeroDivisionError as err :
    print(err)
    sys.exit(2)
print(res)





