class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_table = {}
        s_table = {}

        for ch in s:
            s_table[ch] = s_table[ch] + 1 if ch in s_table else 1

        for ch in t:
            t_table[ch] = t_table[ch] + 1 if ch in t_table else 1

        for ch, count in s_table.items():
            if ch not in t_table:
                return False

            if t_table[ch] != count:
                return False

        for ch, count in t_table.items():
            if ch not in s_table:
                return False

            if s_table[ch] != count:
                return False

        return True