import argparse
import os

from tqdm import tqdm

from mecab_tokenizer import MecabTokenizer


parser = argparse.ArgumentParser()
parser.add_argument(
    "--input_dir",
    default="./corpus",
    type=str,
)

parser.add_argument(
    "--output_dir",
    default="./pretokenized_corpus",
    type=str,
)

args = parser.parse_args()


if not os.path.exists(args.output_dir):
    os.makedirs(args.output_dir)

tokenizer = MecabTokenizer()


# TODO: Multiprocessing
for filename in os.listdir(args.input_dir):
    print("Pretokenizing {}...".format(filename))
    with open(os.path.join(args.input_dir, filename), "r", encoding="utf-8") as f:
        lines = f.read().strip().split("\n")

    with open(os.path.join(args.output_dir, filename), "w", encoding="utf-8") as f:
        for line in tqdm(lines, total=len(lines)):
            f.write(" ".join(tokenizer.tokenize(line)) + "\n")
