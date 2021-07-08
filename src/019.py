# import sys

# with open("noname.txt", 'r') as fr:
#    read = fr.readlines()

# print(read)

# ---------------------
# import sys

# with open("hahaha.txt", 'r') as handle:
# data = handle.readlines()

# print(data)

# --------------------------------
import sys

try:
    with open("hahaha.txt", "r") as handle:
        data = handle.readlines()
except FileNotFoundError as err:
    print("파일이 없음")
    sys.exit()


print(data)

# -----------------------------------
# import sys

# try:
#    val = int(input("Enter: "))
# except ValueError as err:
#    print(err)
#    sys.exit()


# try:
#    print(10/val)
# except ZeroDivisionError as err:
#    print(err)
#    sys.exit()


# try:
#    val = int(input("Enter: "))
#    print(10/val)
# except ZeroDivisionError as err1:
#    print(err1)
#    sys.exit()
# except ValueError as err2:
#    print(err2)
#    sys.exit()
