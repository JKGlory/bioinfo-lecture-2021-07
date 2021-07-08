number = input("Which times table: ")
number = int(number)

if 1 <= number <= 9:
    for i in range(1, 10):
        print("%d * %d = %d" % (number, i, number * i))

else:
    print("What?")


# num =9
# if 0 < num < 10:
#     print('A')
# else:
#     print('B')


# n1 = input('Which times table: ')

# n1 = int(n1)

# print(f"{n1} * {[0:10]} = {n1*(0:10)}")


# for1:
#     for2:
#         if:
#             break(가까이에 있는 반복문을 중지시킨다.=> for2를 중지)

#             continue(뒤에있는 명령문을 가지 않고 가까이에있는 반복문으로 간다.
#             )
