class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        table = {}

        for num in nums:
            table[num] = 1 if num not in table else table[num] + 1

        res = 0
        currentMax = 0

        for key, val in table.items():
            if val > currentMax:
                currentMax = val
                res = key

        return res