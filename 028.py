seq = "ATGTTATAG"
comp_data = {"A":"T", "T":"A", "C":"G", "G":"C"}
for i in seq:
    comp_seq += comp_data[s]
print(seq)
print(comp_seq)
print("")


for i in range(len(seq)):
    s = seq[i]
    cs = comp_seq[i]
    bond = "3bond"
    if s =="A" or s =="T":
        bond = "="
    print(f"{s}{bond}{cs}")

    







