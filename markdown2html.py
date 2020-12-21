#!/usr/bin/python3
''' Converts markdown to HTML '''

import sys
import os.path

if __name__ == "__main__":
    ''' Check for correct usage '''
    if len(sys.argv) < 3:
        message = "Usage: ./markdown2html.py README.md README.html"
        print(message, file=sys.stderr)
        exit(1)
    ''' Check if file exists '''
    if not os.path.isfile(sys.argv[1]):
        print("Missing {}".format(sys.argv[1]), file=sys.stderr)
        exit(1)

    with open(sys.argv[1], 'r') as md:
        with open(sys.argv[2], 'w') as html:
            for line in md:
                llist = line.split(' ')
                htmlline = "<h{}>".format(len(llist[0]))
                for word in llist[1:-1]:
                    htmlline += word + ' '
                htmlline += llist[-1][:-1]
                htmlline += "</h{}>".format(len(llist[0]))
                html.write(htmlline)

    exit(0)
