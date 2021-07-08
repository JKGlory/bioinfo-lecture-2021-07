file_name = "write_sample.txt"

#handle = open(file_name, "w")
#handle.write("Hello\n")
#handle.write(wirte_sample text file\n")


handle = open(file_name, "w")
handle.write("Hello\n")
handle.write("Bioinformatics\n")

with open(file_name, "a") as handle:
    handle.write("Glory\n")


s = "s1,s2,s3"  #csv, tsv
data = s.split(",")
print(data) #['s1' ,'s2', 's3']

with open(file_name, "a") as handle:
    handle.write("\t".join(data)+ "\n")
#   handle.write("**".join(data)+ "\n")
