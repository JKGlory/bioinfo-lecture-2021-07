string_1 = input("Enter s1: ")
string_2 = input("Enter s2: ")

string_1_len = len(string_1)
string_2_len = len(string_2)
if (string_2_len > string_1_len) and (string_1_len % 2 == 1):
    string_3 = string_1 + string_2
else:
    string_3 = string_2 + string_1
print(string_3)
