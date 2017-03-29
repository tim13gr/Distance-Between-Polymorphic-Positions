from collections import Counter


filein = open('inputFileName', 'r')
out = open('outputFileName', 'w')

for line in filein:
    line = line.strip().split('\t')
    multiplier = int(line[1])
    b = list(map(int, line[2:]))
    c = dict(Counter(b))
    distances = []
    counts = []
    for key, value in c.items():
        distances.append(key)
        counts.append(value)
    d2 = list(map(int, distances))
    c2 = list(map(int, counts))
    out.write(str(line[0])+'\t'+str(line[1])+'\t',)
    for x in range(1, 51):
        if x in d2:
            for w, y in enumerate(d2):
                if int(y) == int(x):
                    out.write(str(int(counts[w])*int(line[1]))+'\t',)
        else:
            out.write(str(0)+'\t',)
    out.write('\n')
    
