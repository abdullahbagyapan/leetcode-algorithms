# solution with using 'modulo'

class Solution:
    def isPalindrome(self, x: int) -> bool:
        digits = []

        if (x < 0):
            return False

        while (x != 0):
            digit = x % 10
            x = int(x/10)

            digits.append(digit)


        while ((len(digits) != 0) and (len(digits) != 1)):

            head = digits.pop(0)
            tail = digits.pop(-1)

            if (head != tail):
                return False

        return True