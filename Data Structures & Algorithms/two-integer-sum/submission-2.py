class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # value -> index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:           # did an earlier number pair with this one?
                return [seen[diff], i]
            seen[n] = i                # store this number only after checking
        return []