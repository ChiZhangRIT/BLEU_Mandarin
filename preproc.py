"""
for CSL project, the output format of the GT is
20173816-70,xxxxxxxxxxxxxxxxxxxxxxxx
the output format of the predict is
20173816-70-->xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 

This code is to remove the IDs in front of each line.
"""

import pdb
import os
import sys

ref_filename = sys.argv[1]  # 0 is the script name
tst_filename = sys.argv[2]

# for GT file
with open(ref_filename,'r') as f2:
    sents = f2.readlines() # read lines of input file

with open(ref_filename[:-4]+'_preproc'+ref_filename[-4:],'w') as f1:
	for sent in sents:
		removed = sent.split(' , ', 1)[-1]
		f1.write(removed)

# for prediction file
with open(tst_filename,'r') as f2:
    sents = f2.readlines() # read lines of input file

with open(tst_filename[:-4]+'_preproc'+tst_filename[-4:],'w') as f1:
	for sent in sents:
		removed = sent.split('-->', 1)[-1]
		f1.write(removed)
		
# pdb.set_trace()