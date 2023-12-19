# solution with using string

class Solution:
    def isPalindrome(self, x: int) -> bool:
        str = str(x)

        return str == str[::-1]