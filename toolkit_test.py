"""testing for functions in toolkit.py

Swagata"""

from toolkit import *

assert binary_to_decimal('10110') == 22
assert binary_to_decimal('01001') == 9

pl = [1,2,3]
print(list(reversed(pl)))