def my_len(string):
    cnt = 0
    for i in string:
        cnt += 1
    return cnt


message = input("Enter a string: ")
length = my_len(message)
print("The string length is %d." % (length))


# n1 = input("Enter a string: ")

# if i in n1:
#     print(len(n1))
