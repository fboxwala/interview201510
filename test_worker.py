#
#

import unittest

from worker import word_count


class TestWorker(unittest.TestCase):
    def test_single_word(self):
        self.assertEqual(word_count('WoRd'), {'word': 1})



# Run unit tests.
if __name__ == '__main__':
    unittest.main()
