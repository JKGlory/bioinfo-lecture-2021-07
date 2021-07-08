fr = open("title.txt", "r")
# lines = fr.readlines()  # 다 읽어온다.
for line in fr:
    line = line.strip()
    break
fr.close()
print("The first line is: %s" % (line))
