# Time:  O(logm + logn)
# Space: O(1)
#
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
# 
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example,
# 
# Consider the following matrix:
# 
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.
#

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n
        while left < right:
            mid = left + (right - left) / 2
            if matrix[mid / n][mid % n] >= target:
                right = mid
            else:
                left = mid + 1

        return left < m * n and matrix[left / n][left % n] == target


if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    print Solution().searchMatrix(matrix, 3)
    
    
bool searchMatrix(vector<vector<int> > &matrix, int target) {  
2:            int row = matrix.size();  
3:            if(row ==0) return false;  
4:            int col = matrix[0].size();  
5:            if(col ==0) return false;      
6:            if(target< matrix[0][0]) return false;  
7:            int start = 0, end = row-1;  
8:            while(start<= end)  
9:            {  
10:                 int mid = (start+end)/2;  
11:                 if(matrix[mid][0] == target)  
12:                      return true;  
13:                 else if(matrix[mid][0] < target)  
14:                      start = mid+1;  
15:                 else  
16:                      end = mid-1;  
17:            }  
18:            int targetRow = end;  
19:            start =0;  
20:            end = col-1;  
21:            while(start <=end)  
22:            {  
23:                 int mid = (start+end)/2;  
24:                 if(matrix[targetRow][mid] == target)  
25:                      return true;  
26:                 else if(matrix[targetRow][mid] < target)  
27:                      start = mid+1;  
28:                 else  
29:                      end = mid-1;  
30:            }  
31:            return false;  
32:       }  
