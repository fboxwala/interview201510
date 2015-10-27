# Copyright (C) 2015 Elana Hashman
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

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
