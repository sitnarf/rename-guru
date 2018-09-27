import argparse
from collections import namedtuple
from glob import glob
from distutils.dir_util import copy_tree
from rename_guru.process import process

parser = argparse.ArgumentParser(
    description='Copies the specified folder and replaces all occurrences of given string in camelCase, UPPER_CASE etc. formats.\n' +
                'EXAMPLE: python3 rename_guru.py this_folder that_folder foo bar')
parser.add_argument('source_folder', help='Folder to copy')
parser.add_argument('target_folder', help='Target path')
parser.add_argument('rename', help='Rename this string')
parser.add_argument('to', help='Replace with this string')
args = parser.parse_args()
copy_tree(args.source_folder, args.target_folder)

files = glob(args.target_folder+"/**", recursive=True)

Parameters = namedtuple("Parameters", "real verbose")

process(files, rename=args.rename, to=args.to, parameters=Parameters(real=False, verbose=True))

answer = input("\nPerform changes?!\n")

process(files, rename=args.rename, to=args.to, parameters=Parameters(real=True, verbose=False))

print("Done!")