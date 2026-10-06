class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        all_nums = set()
        for num in nums:
            all_nums.add(num)

        for i in range(n+1):
            if i not in all_nums:
                return i

        return 0