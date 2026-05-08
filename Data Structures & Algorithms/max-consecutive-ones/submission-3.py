class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx = 0
        c = 0

        for i in nums:
            c += 1 if i else -c
            mx = max(c, mx)

        return mx