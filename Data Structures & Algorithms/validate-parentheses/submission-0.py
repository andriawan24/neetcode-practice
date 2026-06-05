class Solution:
    def isValid(self, s: str) -> bool:
        valids = {'}': '{', ')': '(', ']': '['}
        st = []

        for ch in s:
            if ch in valids.values():
                st.append(ch)
            else:
                if st[-1] == valids[ch]:
                    st.pop()
                else:
                    return False

        return True
