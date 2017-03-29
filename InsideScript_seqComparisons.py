'''Compares 2 allele sequences of EQUAL LENGTH s1 and s2 for polymorphic positions and counts the bases between them,
ignores leading and trailing dots(.) and counts consecutive polymorphic positions as a block.
This script can be used to test the behavior of DistBtwnPolymorhicPos.py.
Type your sequences between [''] on line 7,8 and run.'''

from operator import itemgetter
from itertools import groupby
from operator import itemgetter 

s1 = ['AA.TTTGGG.GTA.AAA'] # add seq1
s2 = ['..ATTGG..AGAAT...'] # add seq2
seq1 = ""
for line in s1:                     #clears trailing newline
    seq1 = seq1 + line.rstrip("\n")
seq2 = ""
for line in s2:
    seq2 = seq2 + line.rstrip("\n")
lenSeq1=len(seq1)                   #counts seq1 length
lenSeq2=len(seq2)                   #counts seq2 length 
if lenSeq1==lenSeq2:                #for equal length seq finds differences and dots
    print('Lenght of seq is: '+ str(lenSeq1)) 
    global s1dotsPos
    s1dotsPos = []
    global s2dotsPos
    s2dotsPos = []
    global polPos
    polPos =[]      
    for i in range(0,len(seq1)):   #creates new list with the dots and polymorphic positions
        if seq1[i] == '.':
            s1dotsPos.append(int(i+1))
        if seq2[i] == '.':
            s2dotsPos.append(int(i+1))
        if seq1[i] != seq2[i]:
            polPos.append(int(i+1))
    print('s1dotsPos: '+ str(s1dotsPos))
    print('s2dotsPos: '+ str(s2dotsPos))
    print('polPos: ' + str(polPos))
global s1consecDots
s1consecDots = []
global finals1Dots
finals1Dots = []
if s1dotsPos:        # removes leading and trailing dots
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
    print('finals1Dots: ' + str(finals1Dots))
else:
    s1consecDots = []
    print('finals1Dots: ' + str(s1consecDots))

global s2consecDots
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
    print('finals2Dots: ' + str(finals2Dots))
               
else:
    s2consecDots = []
    print('finals2Dots: ' + str(s2consecDots))
 
newpolPos = []
for i in polPos:
    if i in finals1Dots:
        finals1Dots.remove(i)
    elif i in finals2Dots:
        finals2Dots.remove(i)
    else:
        newpolPos.append(i)
print('newpol: ' + str(newpolPos))
fdist = []                   # calculates the distances between polymorphic positions.Treats consetuvite polPositions as block
for i in range(len(newpolPos)-1): # -1 is used because in python 0 is 1, 1 is 2, 2 is 3 etc
               if int(newpolPos[i+1] - newpolPos[i] -1) !=0: # -1 is used to avoid confusion in distance output. Example: we want to see that bases distance between A and G in ATTG is 2 and not 3
                      fdist.append(newpolPos[i+1] - newpolPos[i] -1)
print('Distances between Polymorphic Postion: ' + str(fdist).strip('[]'))

