# Distance-Between-Polymorphic-Positions

Calculates the distances between polymorphic positions on HLA-gene using a starting msf from IMGT.

Usage of DistBtwnPolymorhicPos.py script in the mainScript folder

1.Prepare a folder, add yourfile.msf and this script. 
2.In the command line change directory to the new folder 
3.Print: python3 DistBtwnPolymorhicPos.py msfFile genename(example: for HLA-B print only B) binSize(add an integer of the desired binSize)
  command example: python3 DistBtwnPolymorhicPos.py B_gen.msf B 50
4.Optional adjustment: you can adjust the part of the sequence where the script will compare the 2 sequences. By default it will compare the full length of the sequences. To adjust the length 
change the{ range(0,len(seq1))} found in the line 84 to the range you wish. 
For example: “ for i in range(3000,5000): ” will only compare the 2000 bases part of the sequence between 3000-5000(mind that python starts counting from 0, so 3000 is the base 3001 if you think the first base as position 1)

DistBtwnPolymorhicPos.py script function.

a) script reads the msf file and searches for all allele names
b) creates separate files with the sequence of each allele
c) compares 2 alleles sequences each time for every possible combinations of alleles
d) removes only the leading and trailing periods(.)
e) finds the positions that the 2 alleles sequences have differences ( those are the polymorphic positions)
f) calculates the distance between the  polymorphic positions. Consecutive  polymorphic positions are counted a block
g) The 1st output of the script named results.txt is a 4 columns tab delimited file.
   Column 1and 2 contain the alleles Names that are compared. Column 3 contains the positions where polymorphic positions  were observed      followed by the base of sequence1 and base of sequence2 in that position with comma as separator(5,T,A). Next will be a semicolon character(;) and then the next position(5,T,A;10,G,T;20,C,T).
Column 4 contains the distances between  polymorphic positions semicolon separated(4;9)
h) The 2nd output named distances.txt  is a 2 columns tab delimited file and contains the counts that each distance appears(5	2044 means that distances between polymorphic positions of length 5 appears 2044 times)
i) The 3rd output named binedDistances.txt is a  2 columns tab delimited file and contains the counts that binned distances appears depending of the bin that was chosen(if the binSize was set to 50,
100	19000 means that distances with length in the range of 51-100bases appears 19000 times)
j) creates a folder named AllelesSequence that contains the files of the alleles sequence

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Supporting Scripts

InsideScript_seqComparisons.py can be used to test the way  DistBtwnPolymorhicPos.py calculates the distances between polymorphic positions or to compare 2 sequences of EQUAL LENGTH that you will print or copy inside the script

Usage of InsideScript_seqComparisons.py script in the supportingScripts folder

1. open  InsideScript_seqComparisons.py with a text editor or any other tool for writing in python
2. Type your sequences between [''] on line 7,8 and run the script either from the application you used to edit the script or from the command line  typing: python3  InsideScript_seqComparisons.py 
(you need to cd in the directory you have the InsideScript_seqComparisons.py to run it with the command line)

InsideScript_seqComparisons.py script function.

a) Compares 2 allele sequences of EQUAL LENGTH s1 and s2 for polymorphic positions 
b) Ignores leading and trailing periods(.)
c) Counts the bases between polymorphic positions 
d) Treats consecutive polymorphic positions as a block
e) Prints all major steps on the screen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

truncate.py  correlates the position of a base in a specific allele sequence found from the IMGT site with the position that base is in the msffile

Usage of truncate.py script in the supportingScripts folder 

a) add the name of the file with an allele sequence at the 1line replacing 'alleleSeqFileName'(keep the quotes) 
b) add the specif position you need to correlate at line 8 replacing 4920
c) the script will print on the screen the equivalent position that these base is in the msffile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

freq_no_bins.py script calculates the counts of distances between Polymorphic Positions found taking account the frequency particular gene pairs appears.
freq_with_bins.py does the same calculation but also bins the distances

