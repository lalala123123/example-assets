from pathlib import Path
import argparse
import shutil

output_dir = '.'


def init():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir', default='.')
    args, _ = parser.parse_known_args()
    global output_dir
    output_dir = args.output_dir


def run(files):
    for f in files:
        shutil.copy(str(f), str(Path(output_dir) / Path(f).name))
        print("File %r is copied." % f)
