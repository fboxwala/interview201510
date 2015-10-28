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

from celery import group
from celerysetup import app
from worker import word_count
from collector import reduce_word_count, top_ten


class TestCelery(unittest.TestCase):
    def setUp(self):
        app.conf.CELERY_ALWAYS_EAGER = True

    def test_single_word(self):
        result = word_count.delay('WoRd')
        self.assertEqual(result.get(), {'word': 1})

    def test_group_processing(self):
        FILES = ['test_data/a_modest_proposal.txt',
                 'test_data/metamorphosis.txt',
                 'test_data/leviathan.txt']
        texts = [open(name, 'r').read() for name in FILES]
        top10 = json.loads(open('test_data/combined.json', 'r').read())

        result = group(word_count.s(text) for text in texts).apply_async()
        self.assertEqual(top_ten(reduce_word_count(result.get())), top10)


# Run unit tests.
if __name__ == '__main__':
    unittest.main()
