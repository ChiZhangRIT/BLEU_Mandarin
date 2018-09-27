## PREREQUISITES

* [Python 2.7](https://www.python.org/download/releases/2.7/)
* [Jieba](https://github.com/fxsjy/jieba)

## HOW TO USE

* save the reference sentences in *txt* format, named `ref.txt`. Each line contains one sentence.

* save the predicted sentences in *txt* format, named `tst.txt`. Each line contains one sentence. The number of lines must equal to that in "ref.txt".

* run *jieba_tokenize.py* to tokenize the sentences.
```
python jieba_tokenize.py ref.txt ref_tok.txt
python jieba_tokenize.py tst.txt tst_tok.txt
```

#### Calculate BLEU score based on [multi_bleu](https://github.com/karpathy/neuraltalk/blob/master/eval/multi-bleu.perl)

```
perl multi-bleu.perl ref_tok.txt < tst_tok.txt
```

#### Alternatively, calculate BLEU score based on [COCO-EVAL](https://github.com/tylin/coco-caption/tree/master/pycocoevalcap):
```
python caption_eval.py ref_tok.txt tst_tok.txt 
```

Note: For CSL project, after tokenization we may need to do some pre-processing to remove the video and signer IDs in front of each line:
```
python preproc.py data/ground_truth_tok.txt data/predicted.txt
perl multi-bleu.perl data/ground_truth_tok.txt < data/predicted.txt  # use multi_bleu 
python caption_eval.py data/ground_truth_tok.txt data/predicted.txt  # use coco-eval
```