class Solution:
    def isNumber(self, s):
        seen_digit = False
        seen_dot = False
        seen_e = False
        digit_after_e = True

        for i, ch in enumerate(s):

            if ch.isdigit():
                seen_digit = True

                if seen_e:
                    digit_after_e = True

            elif ch == '.':
                if seen_dot or seen_e:
                    return False

                seen_dot = True

            elif ch == 'e' or ch == 'E':
                if seen_e or not seen_digit:
                    return False

                seen_e = True
                digit_after_e = False

            elif ch == '+' or ch == '-':
                if i != 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False

            else:
                return False

        return seen_digit and digit_after_e