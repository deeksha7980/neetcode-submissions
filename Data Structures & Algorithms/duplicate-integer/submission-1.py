from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums)==0:
            return False
        count=Counter(nums)
        nums_l=[j for i,j in count.items()]
        if max(nums_l)>1:
            return True
        else:
            return False