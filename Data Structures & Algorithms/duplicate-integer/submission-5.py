class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False 
        new_nums = []
        new_nums.append(nums[0])
        for num in nums[1:]:
            if (num in new_nums):
                return True
            else:
                new_nums.append(num) 

        return False