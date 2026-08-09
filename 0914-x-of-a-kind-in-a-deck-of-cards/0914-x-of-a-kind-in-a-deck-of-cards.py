from collections import Counter
import math
from functools import reduce

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counts = Counter(deck).values()
        overall_gcd = reduce(math.gcd, counts)
        return overall_gcd > 1