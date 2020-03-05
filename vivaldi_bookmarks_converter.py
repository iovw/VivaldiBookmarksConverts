#!/usr/bin/env python3

# Copyright (c) 2020 iovw
# All rights reserved.


import sys
import json
import argparse as ap
from lxml import etree as E


def generate(e: dict):
    ty = e['type']
    if ty == 'url':
        a = E.Element('a', attrib={'href': e['url'],
                                   #    'add_date': '0',
                                   #    'last_modified': '0'
                                   })
        a.text = e['name']
        return '<DT>'+E.tostring(a, encoding='unicode')+'\n'
    elif ty == 'folder':
        header = E.Element(
            'h3',
            # attrib={'add_date': '0', 'last_modified': '0'}
        )
        header.text = e['name']
        content = '<DT>' +\
            E.tostring(header, encoding='unicode') +\
            '\n<DL><p>\n'
        for i in e['children']:
            content += generate(i)
        content += '</DL><p>'
        return content


if __name__ == "__main__":
    parser = ap.ArgumentParser(
        description="Convert vivaldi browser bookmakets to firefox bookmarkets format.")
    required = parser.add_argument_group('required arguments')
    required.add_argument('-f', '--file',
                          type=ap.FileType('r'),
                          required=True,
                          help='the path of vivaldi bookmarkets')
    parser.add_argument('-o', '--out',
                        type=ap.FileType('w'),
                        default=sys.stdout,
                        required=False,
                        help='the path of output')
    args = parser.parse_args()
    inp = args.file

    inp = json.load(inp)

    inp = inp['roots']['bookmark_bar']
    r = generate(inp)
    out_content = '''<!DOCTYPE NETSCAPE-Bookmark-file-1>
        <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
        <TITLE>Bookmarks</TITLE>
        <H1>Bookmarks Menu</H1>
        <DL><p>''' +\
        r +\
        '\n</DL>'
    args.out.write(out_content)
    args.out.close()
