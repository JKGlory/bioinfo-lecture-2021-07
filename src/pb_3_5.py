fr = open("sequence.protein.2.fasta", "r")
line_count = 0
for line in fr:
    line = line.strip()
    if line_count == 1:
        break
    line_count += 1
fr.close()

print("The second line is: %s" % (line))
