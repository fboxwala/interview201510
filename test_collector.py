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

from collector import reduce_word_count, top_ten


class TestReduce(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reduce_word_count([]), {})

    def test_single_dict(self):
        self.assertEqual(reduce_word_count([{'word': 1}]), {'word': 1})

    def test_two_dicts(self):
        self.assertEqual(
            reduce_word_count([{'word': 1}, {'word': 2}]), {'word': 3})


class TestTopTen(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(top_ten({}), {})

    def test_single_dict(self):
        self.assertEqual(top_ten({'word': 1}), {'word': 1})

    def test_AModestProposal(self):
        word_map = json.load(open('test_data/a_modest_proposal.json', 'r'))
        top10 = json.load(open('test_data/a_modest_proposal_top_10.json', 'r'))
        self.assertEqual(top_ten(word_map), top10)


# Run unit tests.
if __name__ == '__main__':
    unittest.main()
