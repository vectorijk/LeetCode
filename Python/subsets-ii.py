# Time:  O(n * 2^n)
# Space: O(1)

# Given a collection of integers that might contain duplicates, S, return all possible subsets.
# 
# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If S = [1,2,2], a solution is:
# 
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S.sort()
        ans,res=[],[]
        self.solve(0, len(S), S, res, ans)
        return ans
                      
    def solve(self,cur,n,S,res,ans):           
        ans.append(res[:])
        i=cur
        while i < n:
            res.append(S[i])
            self.solve(i+1, len(S), S, res, ans)
            while i+1<n and S[i]==S[i+1]: i+=1
            res.pop()
            i+=1


class Solution(object):
    def subsetsWithDup(self, S):
        S.sort()
        ans,res=[],[]
        self.solve(0, len(S), S, res, ans)
        return ans
                      
    def solve(self,cur,n,S,res,ans):           
        ans.append(res[:])
        for i in range(cur, n):
            if i > cur and S[i]==S[i-1]:
                continue
            res.append(S[i])
            self.solve(i+1, len(S), S, res, ans)
            res.pop()
            
public class SubsetsII {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        if(nums == null || nums.length == 0) return result;
        //这里就需要排序了，给以后跳过重复数字埋下伏笔
        Arrays.sort(nums);
        //剩下都是一样的
        List<Integer> list = new ArrayList<>();
        dfs(result, list, 0, nums);
        return result;
    }
    public void dfs(List<List<Integer>> result, List<Integer> list, int start, int[] nums){
        result.add(new ArrayList<>(list));
        for(int i = start; i < nums.length; i++){
            //关键就在这一句，每次循环起始的数字不能和之前重复。
            if(i > start && nums[i] == nums[i-1]) continue;
            list.add(nums[i]);
            dfs(result, list, i+1, nums);
            list.remove(list.size()-1);
        }
    }
}

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = [[]]
        previous_size = 0
        for i in xrange(len(nums)):
            size = len(result)
            for j in xrange(size):
                # Only union non-duplicate element or new union set.
                if i == 0 or nums[i] != nums[i - 1] or j >= previous_size:
                    result.append(list(result[j]))
                    result[-1].append(nums[i])
            previous_size = size
        return result


# Time:  O(n * 2^n) ~ O((n * 2^n)^2)
# Space: O(1)
class Solution2(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        i, count = 0, 1 << len(nums)
        nums.sort()
        
        while i < count:
            cur = []
            for j in xrange(len(nums)):
                if i & 1 << j:
                    cur.append(nums[j])
            if cur not in result:
                result.append(cur)
            i += 1
            
        return result


# Time:  O(n * 2^n) ~ O((n * 2^n)^2)
# Space: O(1)
class Solution3(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.subsetsWithDupRecu(result, [], sorted(nums))
        return result
    
    def subsetsWithDupRecu(self, result, cur, nums):
        if not nums:
            if cur not in result:
                result.append(cur)
        else:
            self.subsetsWithDupRecu(result, cur, nums[1:])
            self.subsetsWithDupRecu(result, cur + [nums[0]], nums[1:])

   
if __name__ == "__main__":
    print Solution().subsetsWithDup([1, 2, 2])
