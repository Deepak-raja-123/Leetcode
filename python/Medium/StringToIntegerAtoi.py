class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)

        # 1. Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # 2. Check sign
        sign = 1

        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # 3. Read digits
        result = 0

        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')

            result = result * 10 + digit

            i += 1

        result *= sign

        # 4. Clamp to 32-bit signed integer range
        INT_MIN = -2147483648
        INT_MAX = 2147483647

        if result < INT_MIN:
            return INT_MIN

        if result > INT_MAX:
            return INT_MAX

        return result