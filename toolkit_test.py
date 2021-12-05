"""testing for functions in toolkit.py

Swagata"""

from typing import Counter
from toolkit import *

assert binary_to_decimal('10110') == 22
assert binary_to_decimal('01001') == 9

assert str_to_tup('3, 4') == (3,4)
assert str_to_tup('4,5,6') == (4,5,6)

l = [11,2,3,2]
import collections

print(Counter(l))