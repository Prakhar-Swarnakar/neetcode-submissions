from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        best = nums[0]
        for x in nums:
            cur_sum = cur_sum + x  
            if cur_sum > best:
                best = cur_sum
            if cur_sum < 0:
                cur_sum = 0
        return best