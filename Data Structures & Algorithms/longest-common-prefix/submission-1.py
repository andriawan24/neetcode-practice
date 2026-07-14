class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ""
        min_len = len(strs[0])

        for i in range(1, len(strs)):
            min_len = min(min_len, len(strs[i]))

        for i in range(0, min_len):
            temp = strs[0][i]

            for j in range(1, len(strs)):
                if temp != strs[j][i]:
                    return longest_prefix

            longest_prefix += temp

        return longest_prefix