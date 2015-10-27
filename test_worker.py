#
#

import json
import unittest

from worker import word_count


class TestWorker(unittest.TestCase):
    def test_single_word(self):
        self.assertEqual(word_count('WoRd'), {'word': 1})

    def test_no_empty_strings(self):
        self.assertEqual(word_count(''), {})

    def test_punctuation_only(self):
        self.assertEqual(word_count(' .;$!!!!   	"""'), {})

    def test_on_a_link(self):
        self.assertEqual(
            word_count('http://hashman.ca'),
            {
                'http': 1,
                'hashman': 1,
                'ca': 1
            })

    def test_AModestProposal(self):
        book = open('test_data/a_modest_proposal.txt', 'r')
        text = book.read()

        word_map = json.load(open('test_data/a_modest_proposal.json', 'r'))

        self.assertEqual(word_count(text), word_map)


# Run unit tests.
if __name__ == '__main__':
    unittest.main()
