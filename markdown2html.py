#!/usr/bin/python3
import sys
import os.path

''' Converts markdown to HTML '''


''' Part 0 '''
''' Check for correct usage '''
if len(sys.argv) < 2:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    exit(1)
''' Check if file exists '''
if not os.path.isfile(sys.argv[1]):
    message = "Missing " + sys.argv[1]
    print(message, file=sys.stderr)
    exit(1)

exit(0)