import argparse
import pathlib
import sys

from . import __version__
from dirtree.dirtree import DirectoryTree


def main():
    args = parse_cmd_arguments()
    root_dir = pathlib.Path(args.root_dir)
    if not root_dir.is_dir():
        print("the specified root_dir doesn't exists")
        sys.exit()
    tree = DirectoryTree(
        root_dir, dir_only=args.dir_only, output_file=args.output_file
    )
    tree.generate()


def parse_cmd_arguments():
    parser = argparse.ArgumentParser(
        prog="dirtree",
        description="directory tree generator"
    )
    parser.version = f"dirtree v{__version__}"
    parser.add_argument("-v", "--version", action="version")
    parser.add_argument(
        "root_dir",
        metavar="ROOT_DIR",
        nargs="?",
        default=".",
        help="generate a full directory tree starting from ROOT_DIR",
    )
    parser.add_argument(
        "-d",
        "--dir-only",
        action="store_true",
        help="generate directory only tree"
    )
    parser.add_argument(
        "-o",
        "--output-file",
        metavar="OUTPUT_FILE",
        nargs="?",
        default=sys.stdout,
        help="generate a full directory tree and save it to a file"
    )

    return parser.parse_args()
