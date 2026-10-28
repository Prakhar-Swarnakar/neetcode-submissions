class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elementCounter = {} # @value -> count
        for n in nums:
            if n in elementCounter:
                elementCounter[n] += 1
            else:
                elementCounter[n] = 1

        # bucket[c] holds every value that appears exactly c times
        bucket = [[] for _ in range(len(nums) + 1)]
        for n, count in elementCounter.items():
            bucket[count].append(n)

        # collect values from the highest count down, keep the first k
        result = []
        for values in range(len(bucket) - 1, 0, -1):
            n = bucket[values]
            result.extend(n)
        return result[:k]
        