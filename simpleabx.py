import argparse
from subprocess import Popen
from subprocess import DEVNULL
import random
import sys

PLAYER = 'mpv'


def play(file):
    return Popen([PLAYER, file], stdin=DEVNULL, stdout=DEVNULL,
                 stderr=DEVNULL)

parser = argparse.ArgumentParser()
parser.add_argument('file_a')
parser.add_argument('file_b')
args = parser.parse_args()

process = play(args.file_a)
input('A')
process.terminate()

process = play(args.file_b)
input('B')
process.terminate()

letter_x, file_x = random.choice([('A', args.file_a), ('B', args.file_b)])

process = play(file_x)
choice = input('X? ').upper()
process.terminate()

print(choice)
if choice not in ['A', 'B']:
    sys.exit(2)
if choice == letter_x:
    sys.exit(0)
else:
    sys.exit(1)
