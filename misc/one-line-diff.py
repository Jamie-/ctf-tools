#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='Diff utility for single lines with colour highlighting.')
parser.add_argument('line1', help='First line.')
parser.add_argument('line2', help='Second line.')
args = parser.parse_args()

l1 = list(args.line1)
l2 = list(args.line2)

diffs = []

for i in range(max(len(l1), len(l2))):
    try:
        if l1[i] != l2[i]:
            diffs.append(i)
    except IndexError:
        diffs.append(i)

def pprint(line):
    out = ''
    for i in range(len(line)):
        if i in diffs:
            out += '\033[1;31m' # RED
            out += line[i]
            out += '\033[0;0m' # RESET
        else:
            out += line[i]
    print(out)

if len(diffs) is 0:
    print('Lines do not differ.')
else:
    print('Lines differ.')
    pprint(l1)
    pprint(l2)
