## HOW TO USE

* save the reference sentences in *txt* format, named `ref.txt`. Difference sentences shoule be in different lines.

* save the predicted sentences in *txt* format, named `tst.txt`. Difference sentences shoule be in different lines. The number of total lines must equal to that in "ref.txt".

* run *jieba_tokenize.py* to tokenize the sentences.
```
python jieba_tokenize.py ref.txt ref_tok.txt
python jieba_tokenize.py tst.txt tst_tok.txt
```

* calculate BLEU score with the following
```
perl multi-bleu.perl ref_tok.txt < tst_tok.txt
```

Alternatively, use COCOeval:
```
python caption_eval.py 
```