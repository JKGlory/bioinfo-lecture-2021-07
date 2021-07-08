fr = open("sequence.protein.fasta", "r")
seq_list = list()
for line in fr:
    line = line.strip()
    if line == "":
        continue
    seq_list.append(line)
fr.close()

seq = "\n".join(seq_list)  # (...)\n(...)\n(...) #seq_list는 string이여야만 한다.
fw = open("sequence.protein.2.fasta", "w")
fw.write("%s\n" % (seq))  # (...)\n(...)\n(...)\n  =>  마지막\n을 추가시키는 cmd
fw.close()
