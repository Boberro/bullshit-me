# -*- coding: utf-8 -*-
import sys
from os import listdir
from os.path import isfile, join
from io import open
import re
from random import choice

HELP_TEXT = '''Bullshit Me, bullshit monthly report generator
Usage:
python bullshit_me.py [number_of_lines] [filename1] [filename2] ... [filename10]
number_of_lines - how many elements your report will have
filename1, filename2 etc - files that define random words used in report'''


def main():
    # check parameters
    params = sys.argv

    if len(params) == 2 and params[1] in ['--help', '-h']:
        return HELP_TEXT
    elif len(params) < 3:
        print '*** Try --help parameter ***'
        print '*** Trying to use default parameters: 60 words.1.txt words.2.txt words.3.txt words.4.txt ***'
        params = ['', '60', 'words.1.txt', 'words.2.txt', 'words.3.txt', 'words.4.txt']

    # load files
    number_of_lines = int(params[1])
    filenames = params[2:]

    word_lists = []
    for _i, filename in enumerate(filenames):
        with open(filename, 'r', encoding="utf-8") as f:
            _lines = f.read().splitlines()
            if not (_lines[0] in [u'[location]']):
                word_lists.append(_lines)
            else:
                _path = _lines[1]
                _regex = _lines[2]
                _files = [_f for _f in listdir(_path) if isfile(join(_path, _f))]
                _lines = get_data_from_filenames(_files, _regex)
                word_lists.append(_lines)

    sentences = []
    # for each line
    for _ in range(1, number_of_lines):
        _words = []
        # for each file
        for word_list in word_lists:
            # select a word
            _words.append(choice(word_list))
        sentences.append(u' '.join(_words))

    return u'\n'.join(sentences)


def get_data_from_filenames(files, regex):
    r = re.compile(regex)
    return [m.group(1) for m in (r.match(filename) for filename in files) if m]


if __name__ == '__main__':
    print main()









# add words



# return bullshit
