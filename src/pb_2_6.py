def my_reverse(string):
    return string[::-1]


message = input("Enter a string: ")

reverse = my_reverse(message)
print("Reversed string: %s" % reverse)
