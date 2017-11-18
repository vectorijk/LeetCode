# Time:  O(n)
# Space: O(1)
#
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.
# 
# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
# 
# The number of ways decoding "12" is 2.
#

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        dp = [0] * (len(s) + 1)
        dp[1] = 0 if s[0] == '0' else 1
        dp[0] = 1
        for i in range(1, len(s)):
            idx = i + 1
            if int(s[i]) >= 1 and int(s[i]) <= 9:
                dp[idx] += dp[idx-1]
            if int(s[i-1] + s[i]) >= 10 and int(s[i-1] + s[i]) <= 26:
                dp[idx] += dp[idx-2] 
        # print dp
        return dp[-1]

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s[0] == '0':
            return 0
        prev, prev_prev = 1, 0
        for i in xrange(len(s)):
            cur = 0
            if s[i] != '0':
                cur = prev
            if i > 0 and (s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6')):
                cur += prev_prev
            prev, prev_prev = cur, prev
        return prev


if __name__ == "__main__":
    for i in ["0", "10", "10", "103", "1032", "10323"]:
        print Solution().numDecodings(i)
