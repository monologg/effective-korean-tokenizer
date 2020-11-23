# Effective Korean Tokenizer

Effective method for building Korean Tokenizer


## Requirements
`NOTE`: Before the installation, check if [mecab-ko-dic](https://bitbucket.org/eunjeon/mecab-ko-dic/src/master/) is already configured.

```bash
$ pip3 install -r requirements.txt
```

## How to

1. Make corpus directory and put corpus files

```bash
$ mkdir -p corpus
```

2. Pretokenize corpus with Mecab

```bash
$ python3 src/mecab_pretokenize.py --input_dir corpus --output_dir pretokenized_corpus
```

3. Train Wordpiece

```bash
$ mkdir -p vocab
$ python3 src/train_bertwordpiece.py --files 'pretokenized_corpus/*' --out vocab
```
