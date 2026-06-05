class Solution:
    def isValid(self, s: str) -> bool:
        valids = {'}': '{', ')': '(', ']': '['}
        st = []

        for ch in s:
            if ch in valids:
                if st[-1] == valids[ch]:
                    st.pop()
                else:
                    return False
            else:
                st.append(ch)

        return True
