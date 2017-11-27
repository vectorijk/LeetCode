# Time:  O(n)
# Space: O(n)

# In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.
#
# Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.
#
# Return the result as a list of indices representing the starting position of each interval (0-indexed).
# If there are multiple answers, return the lexicographically smallest one.
#
# Example:
# Input: [1,2,1,2,6,7,5,1], 2
# Output: [0, 3, 5]
 #   
# Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
# We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
#
# Note:
# - nums.length will be between 1 and 20000.
# - nums[i] will be between 1 and 65535.
# - k will be between 1 and floor(nums.length / 3).


class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        pre_sum = [0] * len(nums)
        pre_sum[0] = nums[0]
        for i in range(1, len(nums)):
            pre_sum[i] = nums[i] + pre_sum[i - 1]
 
        max_index = [[0], [0, k], [0, k, k << 1]]
        max_interval = [pre_sum[k - 1], pre_sum[(k << 1) - 1] - pre_sum[k - 1],
                        pre_sum[3 * k - 1] - pre_sum[(k << 1) - 1]]
 
        max_interval[1] = max_interval[0] + max_interval[1]
        max_interval[2] = max_interval[1] + max_interval[2]
 
        for i in range((k << 1) + 1, len(nums) - k + 1, 1):
            three = pre_sum[i + k - 1] - pre_sum[i - 1]
            two = pre_sum[i - 1] - pre_sum[i - 1 - k]
            one = pre_sum[i - 1 - k] - pre_sum[i - 1 - (k << 1)]
            if one > max_interval[0]:
                max_interval[0] = one
                max_index[0][0] = i - (k << 1)
            if two + max_interval[0] > max_interval[1]:
                max_interval[1] = two + max_interval[0]
                max_index[1] = [max_index[0][0], i - k]
            if max_interval[1] + three > max_interval[2]:
                max_interval[2] = max_interval[1] + three
                max_index[2] = [max_index[1][0], max_index[1][1], i]
        return max_index[2]
# 枚举a~b、b~i、i之后的三段O(n^3)，不用看也知道TLE

# 如何加速?

# 为了方便描述，下面将a~b、b~i、i之后三段称为a、b、i

# 如果我们枚举i，对于当前的这个i，那么我们要是知道a、b两段的和的最大值就好了。

# 换句话说，假设已知a、b两段的和的最大值，那么我们只需要枚举i即可。

# 那么如何只枚举i的时候更新前面两段最大值?

# 注意到i每次向右滑动一个（就是i+1）的时候，

# b段不重复的就可以多了一个元素，即[i-k-1,i-1]，而这个元素要能在最大的a、b段中，必然加上之前的最大值。

# 于是维护max_interval为a段、a、b两段、a、b、i三段的最大值，对应的下标为max_index，初始值max_index = [[0], [0, k], [0, k, k << 1]]

# 然后枚举i，范围为：[(k << 1) + 1, len(nums) – k + 1)

# 分别计算现在新增的三段：pre_sum为累计和

# three = pre_sum[i + k – 1] – pre_sum[i – 1]
# two = pre_sum[i – 1] – pre_sum[i – 1 – k]
# one = pre_sum[i – 1 – k] – pre_sum[i – 1 – (k << 1)]
# 然后更新各段维护的最大值和其下标即可。

# 第一次写的时候下标max_index更新错了。因为可能第一段更新而第二段没有更新，第三段更新这种，然后max_index[0]和max_index[1]的区间是重叠的。改了就对了。
       

class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        accu = [0]
        for num in nums:
            accu.append(accu[-1]+num)
       
        left_pos = [0] * n
        total = accu[k]-accu[0]
        for i in xrange(k, n):
            if accu[i+1]-accu[i+1-k] > total:
                left_pos[i] = i+1-k
                total = accu[i+1]-accu[i+1-k]
            else:
                left_pos[i] = left_pos[i-1]
        
        right_pos = [n-k] * n
        total = accu[n]-accu[n-k]
        for i in reversed(xrange(n-k)):
            if accu[i+k]-accu[i] > total:
                right_pos[i] = i;
                total = accu[i+k]-accu[i]
            else:
                right_pos[i] = right_pos[i+1]
        
        result, max_sum = [], 0
        for i in xrange(k, n-2*k+1):
            left, right = left_pos[i-1], right_pos[i+k]
            total = (accu[i+k]-accu[i]) + \
                    (accu[left+k]-accu[left]) + \
                    (accu[right+k]-accu[right])
            if total > max_sum:
                max_sum = total
                result = [left, i, right]
        return result
