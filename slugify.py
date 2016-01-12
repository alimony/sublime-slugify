# encoding: utf-8

'''
The slugify() function lives in a separate file so it can be tested by tests.py
'''

from __future__ import unicode_literals

import re
from unicodedata import normalize

_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.;:]+')


def slugify(s, separator='-'):
    '''This function is from http://flask.pocoo.org/snippets/5/'''
    result = []
    for word in _punct_re.split(s.lower()):
        word = normalize('NFKD', word).encode('ascii', 'ignore').decode('ascii')
        if word:
            result.append(word)

    output = separator.join(result)

    return output
