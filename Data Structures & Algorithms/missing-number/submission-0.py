class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        all_nums = set()
        for i in range(n+1):
            all_nums.add(i)

        for num in nums:
            all_nums.remove(num)

        return all_nums.pop()