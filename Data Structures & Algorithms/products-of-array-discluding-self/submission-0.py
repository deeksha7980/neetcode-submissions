class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        li=[]
        if len(nums)==0:
            return []
        else:
            for i in range(len(nums)):
                if nums[i]==0:
                    nums.remove(nums[i])
                    a=math.prod(nums)
                    li.append(a)
                    nums.insert(i,0)
                else:
                    b=math.prod(nums)//nums[i]
                    li.append(b)
        return(li)
