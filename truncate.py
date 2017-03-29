filein = open('alleleSeqFileName', 'r')

seq = ''
for line in filein:
    seq = seq + line.rstrip('\n')

dotlist = []
counter = 0
for i in seq:
    if i == '.':
        dotlist.append(0)
    else:
        counter = counter + 1
        dotlist.append(counter)

for position, base in enumerate(dotlist):
    if base == 4920:
        print(position)
