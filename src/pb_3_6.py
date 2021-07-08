fr = open("sequence.protein.2.fasta", "r")
title = ""
seq_list = list()
for line in fr:
    line = line.strip()
    if line == "":
        continue
    if line[0] != ">":
        seq_list.append(line)
    else:
        title = line
fr.close()

seq = "".join(seq_list)
print("title: %s" % (title))
print("seq: %s" % (seq))
