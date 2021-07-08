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
while True:
    position = input("Position: ")
    if position == "XXX":
        print("Okay, I will stop.")
        break
    else:
        position = int(position)
        seq_len = len(seq)
        if 1 <= position <= seq_len - 3:
            sliced_seq = seq[position : position + 3]
            print("Three amino acids: %s" % (sliced_seq))
        else:
            print("Invalid range position value.")
