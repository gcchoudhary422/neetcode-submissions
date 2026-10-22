class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False 
        new_nums = set()
        new_nums.add(nums[0])
        for num in nums[1:]:
            if (num in new_nums):
                return True
            else:
                new_nums.add(num) 

        return False