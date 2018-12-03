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
parser.add_argument('--perform', action="store_true", help='Don\'t ask and perform changes automatically')
args = parser.parse_args()
copy_tree(args.source_folder, args.target_folder)

Parameters = namedtuple("Parameters", "real verbose")

if not args.perform:
    process(args.target_folder, rename=args.rename, to=args.to, parameters=Parameters(real=False, verbose=True))
    answer = input("\nPerform changes?!\n")

process(args.target_folder, rename=args.rename, to=args.to, parameters=Parameters(real=True, verbose=False))

print("Done!")