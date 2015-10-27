#
#

import re

def word_count(text_blob):
    word_map = {}
    tokens = [x.lower() for x in re.split('[^a-zA-Z0-9]+', text_blob)]

    for token in tokens:
        if word_map.get(token) is None:
            word_map[token] = 1
        else:
            word_map[token] += 1

    return word_map
