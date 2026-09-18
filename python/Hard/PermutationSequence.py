class Solution:
    def getPermutation(self, n, k):
        numbers = [str(i) for i in range(1, n + 1)]
        result = []

        k -= 1

        for i in range(n):
            factorial = 1

            for j in range(1, n - i):
                factorial *= j

            index = k // factorial

            result.append(numbers[index])
            numbers.pop(index)

            k %= factorial

        return "".join(result)