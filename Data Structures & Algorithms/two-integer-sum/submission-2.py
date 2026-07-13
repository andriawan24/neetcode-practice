class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}

        for i in range(len(nums)):
            sub = target - nums[i]

            if sub in table:
                return [table[sub], i]

            table[nums[i]] = i

        return []