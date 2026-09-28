class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
        # h=set(nums)
        # if len(nums)==len(h):
        #     return False
        # return True
        # for num in nums:
        #     if num in h:
        #         return True
        #     h.add(num)
        # return False

        
        