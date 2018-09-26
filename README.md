HOW TO USE

1. save the reference sentences in txt format, named "ref.txt". Difference sentences shoule be in different lines.

2. save the predicted sentences in txt format, named "tst.txt". Difference sentences shoule be in different lines. The number of total lines must equal to that in "ref.txt".

3. run 'jieba_tokenize.py' to tokenize the sentences.
```
python jieba_tokenize.py ref.txt ref_tok.txt
python jieba_tokenize.py tst.txt tst_tok.txt
```

4. calculate BLEU score with the following
```
perl multi-bleu.perl ref_tok.txt < tst_tok.txt
```