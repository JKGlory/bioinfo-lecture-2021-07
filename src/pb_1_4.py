num_1 = input("Enter a ineger: ")
num_2 = input("Enter another: ")

num_1 = int(num_1)
num_2 = int(num_2)

if num_1 > num_2:
    print("%d is greater than %d." % (num_1, num_2))
elif num_1 < num_2:
    print("%d is less than %d." % (num_1, num_2))
else:
    print("%d is equal to %d." % (num_1, num_2))
