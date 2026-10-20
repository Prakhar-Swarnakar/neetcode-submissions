class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = cur_min = 1
        result = nums[0]
        for x in nums:
            if x < 0:                        # a negative flips which one is biggest
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(x, cur_max * x)    # extend, or restart at x
            cur_min = min(x, cur_min * x)    # a zero restarts both here too
            result = max(result, cur_max)
        return result