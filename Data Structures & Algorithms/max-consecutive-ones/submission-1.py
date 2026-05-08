class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx = 0
        c = 0

        for i in nums:
            if i == 1:
                c += 1
            else:
                mx = max(c, mx)
                c = 0

        return max(mx, c)