class Solution:
    def isValid(self, s: str) -> bool:
        valids = {'}': '{', ')': '(', ']': '['}
        st = []

        for ch in s:
            if ch in valids:
                if len(st) == 0:
                    return False

                if valids[ch] != st[-1]:
                    return False

                st.pop()
            else:
                st.append(ch)

        return len(st) == 0
