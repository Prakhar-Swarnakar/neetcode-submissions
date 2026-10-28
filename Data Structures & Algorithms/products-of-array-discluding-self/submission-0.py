class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #output[i] = (product of everything LEFT of i) × (product of everything RIGHT of i)
        output = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):             # left → right
            output[i] = prefix                 # product of everything before i
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1): # right → left
            output[i] *= suffix                # multiply by product of everything after i
            suffix *= nums[i]

        return output
