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

from __future__ import absolute_import

from celery import group
import sys
from worker import word_count
from collector import reduce_word_count, top_ten


if len(sys.argv) == 1:
    print ("Simple distributed file indexer: counts top 10 words in files in\n"
           "provided directories.\n"
           "Usage: python scheduler.py FILE1 FILE2 ...")
else:
    texts = [open(name, 'r').read() for name in sys.argv[1:]]
    result = group(word_count.s(text) for text in texts).apply_async()
    print top_ten(reduce_word_count(result.get()))
