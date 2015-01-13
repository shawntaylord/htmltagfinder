#!/usr/bin/python

import re
import sys

def nameOfMissingTag(path_to_html_file):
    open_regex = '\<(?P<opentag>[a-zA-Z]+)[^\/]*\>'
    close_regex = '\<\/(?P<closetag>[a-zA-Z]*)\>'

    bracket_dict = {}

    file = open(path_to_html_file, 'r')

    for line in file:
        open_tags = re.findall(open_regex, line)
        closed_tags = re.findall(close_regex, line)
        if open_tags:
            for tag in open_tags:
                if tag in bracket_dict:
                    bracket_dict[tag] += 1
                else:
                    bracket_dict[tag] = 1
        if closed_tags:
            for tag in closed_tags:
                if tag in bracket_dict:
                    bracket_dict[tag] -= 1
                else:
                    bracket_dict[tag] = -1
    # Free up resources from open file
    file.close()

    print bracket_dict

if __name__ == "__main__":
    nameOfMissingTag(sys.argv[1])
