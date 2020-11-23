# Effective Korean Tokenizer

Effective method for building Korean Tokenizer

## Requirements

`NOTE`: Before the installation, check if [mecab-ko-dic](https://bitbucket.org/eunjeon/mecab-ko-dic/src/master/) is already configured.

```bash
$ pip3 install -r requirements.txt
```

## How to

1. Prepare corpus file (e.g. `corpus.txt`)

2. Split corpus file (for multiprocessing)

```bash
$ mkdir corpus
$ split -a 4 -l {$NUM_LINES_PER_FILE} -d {$CORPUS_FILE} ./corpus/data_
```

3. Pretokenize corpus with Mecab

```bash
$ python3 src/mecab_pretokenize.py --input_dir corpus --output_dir pretokenized_corpus --num_processes 16
```

4. Train Wordpiece

```bash
$ mkdir -p vocab
$ python3 src/train_bertwordpiece.py --files 'pretokenized_corpus/*' --out vocab
```
