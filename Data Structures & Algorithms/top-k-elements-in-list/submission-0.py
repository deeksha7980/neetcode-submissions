from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        li = []
        count = Counter(nums)
        # Sort dictionary items by frequency
        sorted_items = sorted(count.items(), key=lambda item: item[1], reverse=True)
        # Append the first k keys
        for i in range(k):
            li.append(sorted_items[i][0])
        print(li)
        return li
