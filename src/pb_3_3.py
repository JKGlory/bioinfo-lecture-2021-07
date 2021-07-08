fr = open("sequence.protein.fasta", "r")
for line in fr:  # fr이 나중에는 시퀀스 데이터가 오는 자리
    line = line.strip()
    if line == "":
        continue
    print(line)
fr.close()
