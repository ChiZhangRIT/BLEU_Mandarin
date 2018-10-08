# encoding=utf-8
'''
Code to tokenize chinese sentences

python jieba_tokenize.py chi_tst.txt chi_tst_out.txt 
'''

import jieba
import sys
import pdb

input_file = sys.argv[1] # input text file
output_file = sys.argv[2] # output file to save results

with open(input_file,'r') as f2:
    sents = f2.readlines() # read lines of input file

lengths = []
with open(output_file,'w') as f1: # to save outputs
    for sent in sents: # one sentence at a time
        # f1.write(sent.strip()+'\t-->\t') # dump original sentence
        words = list(jieba.cut(sent, cut_all=False)) # tokeize sentence using jieba
        lengths.append(len(words)) # keep record of sentence lengths
        for word in words:
            if word == '\n':
                # f1.write(word.encode('utf-8'))
                f1.write(word)
            else:
            	# f1.write(word.encode('utf-8') + ' ') # dump tokenized sentence with tab separation
                f1.write(word + ' ')  
            # pdb.set_trace()


print('Minimum length: ',min(lengths))
print('Maximum length: ',max(lengths))
print('Average length: ',sum(lengths)/len(lengths))
# pdb.set_trace()
