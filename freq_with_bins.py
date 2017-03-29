filein = open('inputFileName', 'r')
out = open('outFileName','w')
for x in range(1,3395,50):
    c = []
    filein.seek(0,0)
    out.write(str(x)+'\t',)
    for line in filein:
        line = line.strip().split('\t')
        multiplier = int(line[1])
        b = list(map(int, line[2:]))
        counts = 0
        for i in b:
            if int(x)<= i <int(x+50):
                counts += 1
        counts = counts*multiplier
        c.append(counts)
    d = sum(c)
    out.write(str(d),)
    out.write('\n')
    

