class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        res = x
        rev = 0
        while x > 0:
            l = x % 10
            rev = (rev * 10) + l 
            x //= 10

        return rev == res