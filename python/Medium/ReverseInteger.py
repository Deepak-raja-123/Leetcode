class Solution:
    def reverse(self, x):
        result = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            # Check 32-bit overflow before adding digit
            if result > 214748364 or (
                result == 214748364 and digit > 7
            ):
                return 0

            result = result * 10 + digit

        return sign * result