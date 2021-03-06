# Time:  O(n)
# Space: O(1)
#
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):
#

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        
        for i in range(0, n):
            if knows(ans, i):
                ans = i
                
        for i in range(0, n):
            if i != ans and knows(ans, i):
                return -1
            if i != ans and not knows(i, ans):
                return -1
        return ans
    
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0
        # Find the candidate.
        for i in xrange(1, n):
            if knows(candidate, i):  # All candidates < i are not celebrity candidates.
                candidate = i
        # Verify the candidate.
        for i in xrange(n):
            if i != candidate and (knows(candidate, i) \
                or not knows(i, candidate)):
                return -1
        return candidate
