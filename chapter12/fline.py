infile = open(r"C:\python2\chapter12\proverbs.txt")
outfile = open(r"C:\python2\chapter12\output.txt","w")

i = 1

for line in infile:
    outfile.write(str(i)+":"+line)
    i = i+1

infile.close()
outfile.close()

