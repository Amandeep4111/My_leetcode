class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        r=dict()
        for i in range(len(nums)):
            c=target-nums[i]
            if c in r:
                return [r[c],i]
            r[nums[i]]=i

        