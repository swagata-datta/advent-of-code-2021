"""testing for functions in toolkit.py

Swagata"""

import collections
from toolkit import *
import re
import numpy as np


assert binary_to_decimal('10110') == 22
assert binary_to_decimal('01001') == 9

assert str_to_tup('3, 4') == (3,4)
assert str_to_tup('4,5,6') == (4,5,6)

dic = {'a':4}

dic['a'] += 1

print(dic)

print(len('NBBBCNCCNBBNBNBBCHBHHBCHB'))

print(len('NBCCNBBBCBHCB'))