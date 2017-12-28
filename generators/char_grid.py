#!/usr/bin/env python3

import argparse
import logging
import string
import random

logging.basicConfig(format='%(asctime)s[%(levelname)8s][%(module)s] %(message)s', datefmt='[%m/%d/%Y][%I:%M:%S %p]')
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description='Letter grid generator.')
parser.add_argument('file', help='File to store the generated grid.')
parser.add_argument('-v', dest='verbose_info', action='store_true', help='Enable info messages.')
parser.add_argument('-vv', dest='verbose_debug', action='store_true', help='Enable info and debug messages.')
parser.add_argument('-s', '--size', dest='size', help='Size of square grid to generate.')
parser.add_argument('-x', '--width', dest='width', help='Width of grid to generate.')
parser.add_argument('-y', '--height', dest='height', help='Height of grid to generate.')
parser.add_argument('-d', '--delimiter', dest='delimiter', help='Delimiter between characters')
args = parser.parse_args()

# Set root logging level
if args.verbose_debug:
    logging.getLogger().setLevel(logging.DEBUG)
elif args.verbose_info:
    logging.getLogger().setLevel(logging.INFO)

# Check sizing arguments
if args.size is None:
    if args.width is None or args.height is None:
        parser.error('You must specify either size or width and height.')
else:
    if not (args.width is None and args.height is None):
        parser.error('You must specify either size or width and height.')

# Fill width and height
if args.size is not None:
    width = int(args.size)
    height = int(args.size)
else:
    width = int(args.width)
    height = int(args.height)

logger.info('Starting grid generation.')

# Generate lines and write to file
with open(args.file, 'w') as f:
    for y in range(height):
        line = ""
        for x in range(width):
            if args.delimiter is not None and x < width - 1:
                line += random.choice(string.ascii_lowercase) + args.delimiter
            else:
                line += random.choice(string.ascii_lowercase)
        f.write('{}\n'.format(line))

logger.info('Generation complete!')
