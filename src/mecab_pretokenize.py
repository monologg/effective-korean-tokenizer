import argparse
import multiprocessing
import os
import time

from mecab_tokenizer import MecabTokenizer


def pretokenize(job_id: int, args: argparse.Namespace):
    def log(*args):
        msg = " ".join(map(str, args))
        print("Job {}:".format(job_id), msg)

    tokenizer = MecabTokenizer()  # one tokenizer for one process

    log("Pretokenize corpus!")
    fnames = sorted(os.listdir(args.input_dir))
    fnames = [f for (i, f) in enumerate(fnames) if i % args.num_processes == job_id]
    start_t = time.time()

    for file_no, fname in enumerate(fnames):
        if file_no > 0:
            elapsed = time.time() - start_t
            log(
                "processed {:}/{:} files ({:.1f}%), ELAPSED: {:}s, ETA: {:}s".format(
                    file_no,
                    len(fnames),
                    100.0 * file_no / len(fnames),
                    int(elapsed),
                    int((len(fnames) - file_no) / (file_no / elapsed)),
                )
            )
        # Pretokenize
        with open(os.path.join(args.input_dir, fname), "r", encoding="utf-8") as f_r:
            with open(os.path.join(args.output_dir, fname), "w", encoding="utf-8") as f_w:
                for line in f_r:
                    f_w.write(" ".join(tokenizer.tokenize(line.strip())))
                    f_w.write("\n")


if __name__ == "__main__":
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
    parser.add_argument("--num_processes", default=4, type=int, help="Parallelize across multiple processes")
    args = parser.parse_args()

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    if args.num_processes == 1:
        pretokenize(0, args)

    else:
        jobs = []
        for i in range(args.num_processes):
            job = multiprocessing.Process(target=pretokenize, args=(i, args))
            jobs.append(job)
            job.start()
        for job in jobs:
            job.join()
