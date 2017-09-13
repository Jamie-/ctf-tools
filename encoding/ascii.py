#!/usr/bin/env python3

import argparse
import re

parser = argparse.ArgumentParser(description='Encode and decode text to ASCII escapes.')
parser.add_argument('--strip', action='store_true', help='Strip whitespace from input.')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--encode', action='store_true', help='Encode a file with ASCII encoding.')
group.add_argument('--decode', action='store_true', help='Decode a file with ASCII encoding.')
parser.add_argument('in_file', help='Input data file.')
parser.add_argument('out_file', nargs='?', help='Output data file.')
args = parser.parse_args()

with open(args.in_file) as in_file:
    input = in_file.read()

if args.strip: # Strip whitespace if --strip given
    input = input.strip()

# ASCII encode a string
def encode(data):
    pattern = re.compile('^[A-Za-z0-9]+$')
    d = list(data)
    out = ''

    for c in d:
        if not pattern.match(c):
            out += '\\x' + format(ord(c), 'x')
        else:
            out += c

    return out

# ASCII decode a string
def decode(data):
    d = list(data)
    i = 0
    out = '' # Out string 'builder'

    while i < len(d):
        if d[i] == '\\':
            out += chr(int(d[i+2] + d[i+3], 16))
            i += 4
        else:
            out += d[i]
            i += 1
    return out

if args.decode:
    output = decode(input)
elif args.encode is True:
    output = encode(input)

# Handle output to file or stdout
if args.out_file is None:
    print(output)
else:
    with open(args.out_file, 'w') as out_file:
        out_file.write(output)
