# Time:  O(n)
# Space: O(1)

# Given an unsorted array return whether an increasing 
# subsequence of length 3 exists or not in the array.

# Formally the function should:
# Return true if there exists i, j, k 
# such that arr[i] < arr[j] < arr[k] 
# given 0 <= i < j < k <= n-1 else return false.
# Your algorithm should run in O(n) time complexity and O(1) space complexity.

# Examples:
# Given [1, 2, 3, 4, 5],
# return true.

# Given [5, 4, 3, 2, 1],
# return false.


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min_num, a, b = float("inf"), float("inf"), float("inf")
        for c in nums:
            if min_num >= c:
                min_num = c
            elif b >= c:
                a, b = min_num, c
            else:  # a < b < c
                return True
        return False

# Time:  O(n * logk)
# Space: O(k)
# Generalization of k-uplet.
class Solution_Generalization(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def increasingKUplet(nums, k):
            inc = [float('inf')] * (k - 1)
            for num in nums:
                i = bisect.bisect_left(inc, num)
                if i >= k - 1:
                    return True
                inc[i] = num
            return k == 0

        return increasingKUplet(nums, 3)
    
    
#这个解法的思路是建立两个数组，forward数组和backward数组，其中forward[i]表示[0, i]之间最小的数，backward[i]表示[i, n-1]之间最大的数，那么对于任意一个位置i，如果满足 forward[i] < nums[i] < backward[i]，则表示这个递增三元子序列存在，举个例子来看吧，比如：
#nums:        8  3  5  1  6
#foward:      8  3  3  1  1
#backward:  8  6  6  6  6
#我们发现数字5满足forward[i] < nums[i] < backward[i]，所以三元子序列存在
class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        if (nums.size() < 3) return false;
        int n = nums.size();
        vector<int> f(n, nums[0]), b(n, nums.back());
        for (int i = 1; i < n; ++i) {
            f[i] = min(f[i - 1], nums[i]);
        }
        for (int i = n - 2; i >= 0; --i) {
            b[i] = max(b[i + 1], nums[i]);
        }
        for (int i = 0; i < n; ++i) {
            if (nums[i] > f[i] && nums[i] < b[i]) return true;
        }
        return false;
    }
};
