# Time:  O(n)
# Space: O(1)
#
# Given n non-negative integers representing an elevation map where the width of each bar is 1,
#  compute how much water it is able to trap after raining.
# 
# For example, 
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
# 
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
# In this case, 6 units of rain water (blue section) are being trapped.
#

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0
        
        left_max = [0] * len(height)
        right_max = [0] * len(height)
        
        left_max[0] = height[0]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i-1], height[i-1])
            
        right_max[-1] = height[-1]
        for i in range(len(height)-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i+1])
            
        
        ans = 0
        for i in range(len(height)):
            if min(left_max[i], right_max[i]) > height[i]:
                ans += min(left_max[i], right_max[i]) - height[i]
            
        return ans

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_left = max_right = ans = 0
        L, R = 0, len(height) - 1
        while L < R:
            if height[L] <= height[R]:
                max_left = max(max_left, height[L])
                ans += max_left - height[L]
                L += 1
            else:
                max_right = max(max_right, height[R])
                ans += max_right - height[R]
                R -= 1
        return ans

class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        result = 0
        top = 0
        for i in xrange(len(A)):
            if A[top] < A[i]:
                top = i
        
        second_top = 0
        for i in xrange(top):
            if A[second_top] < A[i]:
                second_top = i
            result += A[second_top] - A[i]
            
        second_top = len(A) - 1
        for i in reversed(xrange(top, len(A))):
            if A[second_top] < A[i]:
                second_top = i
            result += A[second_top] - A[i]
            
        return result
            
# Time:  O(n)
# Space: O(n)
class Solution2:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        result = 0
        stack = []
        
        for i in xrange(len(A)):
            mid_height = 0
            while stack:
                [pos, height] = stack.pop()
                result += (min(height, A[i]) - mid_height) * (i - pos - 1)
                mid_height = height
                
                if A[i] < height:
                    stack.append([pos, height])
                    break
            stack.append([i, A[i]])
            
        return result
    
if __name__ == "__main__":
    print Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
