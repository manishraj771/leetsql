class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        temp = [0] * 100
        count = 0
        for a, b in dominoes:
            key = a * 10 + b if a <= b else b * 10 + a
            count += temp[key]
            temp[key] += 1
        return count
# class Solution(object):
#     def numEquivDominoPairs(self, dominoes):
#         count = 0
#         for i in range(len(dominoes)):
#             for j in range(i + 1, len(dominoes)):
#                 a, b = dominoes[i]
#                 c, d = dominoes[j]
#                 if (a == c and b == d) or (a == d and b == c):
#                     count += 1
#         return count