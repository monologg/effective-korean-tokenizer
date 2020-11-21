import argparse
import glob

from tokenizers import BertWordPieceTokenizer

parser = argparse.ArgumentParser()
parser.add_argument(
    "--files",
    default=None,
    metavar="path",
    type=str,
    required=True,
    help="The files to use as training; accept '**/*.txt' type of patterns \
                          if enclosed in quotes",
)
parser.add_argument(
    "--out",
    default="./",
    type=str,
    help="Path to the output directory, where the files will be saved",
)
parser.add_argument("--name", default="bert-wordpiece", type=str, help="The name of the output vocab files")
parser.add_argument("--vocab_size", default=31000, type=int, help="Vocab size")
parser.add_argument("--char", default=4000, type=int, help="Number of character in vocab")

args = parser.parse_args()

files = glob.glob(args.files)
if not files:
    print(f"File does not exist: {args.files}")
    exit(1)


# Initialize an empty tokenizer
tokenizer = BertWordPieceTokenizer(
    clean_text=True,
    handle_chinese_chars=True,
    strip_accents=False,
    lowercase=False,
)

# And then train
tokenizer.train(
    files,
    vocab_size=args.vocab_size,
    min_frequency=2,
    show_progress=True,
    special_tokens=["[PAD]", "[UNK]", "[CLS]", "[SEP]", "[MASK]"],
    limit_alphabet=args.char,
    wordpieces_prefix="##",
)

# Save the files
tokenizer.save_model(args.out, args.name)