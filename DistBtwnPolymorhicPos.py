#!/usr/bin/python3
"""Prepare a folder, add yourfile.msf and this script. In the command line change directory to the new folder and
print: python3 DistBtwnPolymorhicPos.py msfFile genename(example: for HLA-B print only B) binsize(add an integer of the desired binSize)"""

import sys
import os, shutil
import re
from itertools import combinations
from operator import itemgetter
from itertools import groupby
from collections import Counter

getdirectory = os.getcwd()
os.chdir(getdirectory)

if len(sys.argv) != 4:
    print('Usage: python3 4DNAcompAndDistCalcIFiles.py msfFile genename(example: for HLA_B print only B) binsize')
    sys.exit()

msffile = sys.argv[1]
genename = sys.argv[2]
sizeOfbin = sys.argv[3]



filedata = None  #replace * with @
with open(msffile, 'r') as file:
    filedata = file.read()
    
filedata = filedata.replace('*', '@') #replace * with @ character

with open(msffile, 'w') as file:
    file.write(filedata)
    
file = open(msffile, 'r') #open msf and find all allele names
readfile = ''
for line in file:
    readfile = readfile + line.rstrip("\n")
findallele = re.findall(r'\b' +re.escape(genename)+'@\S+', readfile)
alleles = sorted(set(findallele))

for element in alleles: #finds specific allele in msf and make new file with the allele seq
    regex = '\\b{0}\\b'.format(element)
    open(element, 'w').writelines([ line for line in open(msffile) if re.findall(regex, line)])

for allele in alleles:  #remove first line
    with open(allele, 'r') as fin:
        data = fin.read(). splitlines(True)
    with open (allele, 'w') as fout:
        fout.writelines(data[1:])

for allele in alleles: # remove 1st column with allele names and whitespases
    with open(allele, 'r') as f:
        global trimlist
        trimlist = []
        for line in f:
            if line.strip():
                trimlist.append(''.join(line.split()[1:]) + '\n')
    finaltrim = ''.join(trimlist)
    with open(allele, 'w') as f:
        f.write(finaltrim)

out = open('output.txt', "w") # compares the 2 sequences
comb = combinations(alleles, 2)
for f1, f2 in comb:
    file1 = open(f1, "r")
    file2 = open(f2, "r")
    seq1 = ""
    for line in file1:
        seq1 = seq1 + line.rstrip("\n")
    seq2 = ""
    for line in file2:
        seq2 = seq2 + line.rstrip("\n")
    lenSeq1=len(seq1)
    lenSeq2=len(seq2)
    if lenSeq1==lenSeq2:
        out.write(f1+'	'+f2+'	')
        global s1dotsPos
        s1dotsPos = []
        global s2dotsPos
        s2dotsPos = []
        global polPos
        polPos =[]
        for i in range(0,len(seq1)):
            if seq1[i] == '.':
                s1dotsPos.append(int(i+1))
            elif seq2[i] == '.':
                s2dotsPos.append(int(i+1))
            if seq1[i] != seq2[i]:
                out.write(str(i+1)+','+seq1[i]+','+seq2[i]+';')
                polPos.append(int(i+1))
        out.write('	')
    s1consecDots = []
    finals1Dots = []
    if s1dotsPos:  # finds only the leading and trailing dots and avoid the comparison of the sequences at that spot
        for key, group in groupby(enumerate(s1dotsPos), lambda i: i[0] - i[1]):
            s1consecDots.append(list(map(itemgetter(1), group)))
        s1consecDotsHead = s1consecDots[0]
        s1consecDotsTail = s1consecDots[-1]
        if 1 in s1consecDotsHead:
            s1consecDotsHeadcheck = s1consecDotsHead        
        else:
            s1consecDotsHeadcheck = []
        if int(len(seq1)) in s1consecDotsTail:
            s1consecDotsTailcheck = s1consecDotsTail
        else:
            s1consecDotsTailcheck = []
        finals1Dots = s1consecDotsHeadcheck + s1consecDotsTailcheck
    else:
        s1consecDots = []
    s2consecDots = []
    finals2Dots = []
    if s2dotsPos:  
        for key, group in groupby(enumerate(s2dotsPos), lambda i: i[0] - i[1]):
            s2consecDots.append(list(map(itemgetter(1), group)))
        s2consecDotsHead = s2consecDots[0]
        s2consecDotsTail = s2consecDots[-1]
        if 1 in s2consecDotsHead:
            s2consecDotsHeadcheck = s2consecDotsHead        
        else:
            s2consecDotsHeadcheck = []
        if int(len(seq1)) in s2consecDotsTail:
            s2consecDotsTailcheck = s2consecDotsTail
        else:
            s2consecDotsTailcheck = []    
        finals2Dots = s2consecDotsHeadcheck + s2consecDotsTailcheck                  
    else:
        s2consecDots = [] 
    newpolPos = []
    for i in polPos:
        if i in finals1Dots:
            finals1Dots.remove(i)
        elif i in finals2Dots:
            finals2Dots.remove(i)
        else:
            newpolPos.append(i)
    for i in range(len(newpolPos)-1):  # counts the distance between Polymorphic Positions. Consecutive base mismatces are treated as a block
        if int(int(newpolPos[i+1]) - int(newpolPos[i]) - int(1)) !=0:
            out.write(str(int(newpolPos[i+1]) - int(newpolPos[i]) - int(1))+ ';')
    out.write('\n')
out.close()
replace1 = open('output.txt', 'r') # replaces @ character with * in the outputFile
replace2 = open('results.txt', 'w')
for line in replace1:
    replace2.write(line.replace('@', '*'))
replace1.close()
replace2.close()

os.remove('output.txt')
    
with open("results.txt", "r") as fin: #keeps column 4 with the distances
    with open("c4results.txt", "w") as fout:
        for line in fin:
            line = line.split('\t')
            del line[0:3]
            fout.write(line[0])
fin.close()
fout.close()

with open('c4results.txt', 'r') as fd: # counts the frequency of each distance
    lines = fd.read()
    lines2 = filter(None, re.compile('[\n;]').split(lines))
    counter = Counter(list(lines2))
    # sorts items
    items = sorted(counter.items(), key=lambda x: int(x[0]))
    # prints desired output
    out = open('distances.txt', 'w')
    #out.write('BaseDistances'+'\t'+'Counts')
    #out.write('\n')
    for k, repetitions in items:
        out.write(str(k)+'\t'+str(repetitions))
        out.write('\n')
    out.close()
os.remove('c4results.txt')

binfile = open('distances.txt', 'r') # bins the counts of distances
binsize = int(sizeOfbin)
output = []
for line in binfile:
    line = line.strip().split('\t')
    distance = int(line[0])
    counts = int(line[1])
    index = int((distance-1) / binsize)
    if index + 1 > len(output):
        num = index + 1
        while num > 0:
            output.append(0)
            num -= 1
    output[index] += counts
binout = open('binedDistances.txt', 'w')
binout.write('binedDistances'+'\t'+'Counts')
binout.write('\n')
for i in range (0, len(output)):
    binout.write(str((i + 1)*binsize)+'\t'+str(output[i]))
    binout.write('\n')
binout.close()

os.makedirs('AllelesSequence') # orginazes the files
for filename in os.listdir(getdirectory):
    if filename.startswith(genename +'@'):
        shutil.move(filename, 'AllelesSequence')

filedata2 = None
with open(msffile, 'r') as file:
    filedata2 = file.read()
filedata2 = filedata2.replace('@', '*')
with open(msffile, 'w') as file:
    file.write(filedata2)





