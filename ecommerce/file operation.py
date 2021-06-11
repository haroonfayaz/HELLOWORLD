import os


infile = open('JASON TECHORONIC.txt', "r")
outfile = open('new1.txt', "w")
for line in infile:
    print(line)
    print(line.rstrip(), file=outfile)

