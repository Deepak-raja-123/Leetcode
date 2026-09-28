class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n

        one_step = 1
        two_step = 2

        for i in range(3, n + 1):
            current = one_step + two_step
            one_step = two_step
            two_step = current

        return two_step