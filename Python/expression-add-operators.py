# Time:  O(4^n)
# Space: O(n)
#
# Given a string that contains only digits 0-9 
# and a target value, return all possibilities 
# to add operators +, -, or * between the digits
# so they evaluate to the target value.
#
# Examples: 
# "123", 6 -> ["1+2+3", "1*2*3"] 
# "232", 8 -> ["2*3+2", "2+3*2"]
# "00", 0 -> ["0+0", "0-0", "0*0"]
# "3456237490", 9191 -> []
#

class Solution(object):
    ###
    # my solution
    ###
#由于运算符的优先级，因此，分为两半，一个是pre为计算的值，一个为val为pre右方还未计算的值.
#对于当前的数x，进行如下的操作可以保证优先级
#加法：pre = pre + val   val = x
#减法： pre =  pre – val   val = -x
#乘法：pre = pre      val = val *x
#当前的第一个数为’0’的情况   计算完后Break
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        def dfs(num, idx, path, ans, target, n, pre, val):
            if idx == n and pre + val == target:
                ans.append(path)
                return
            
            x = 0
            for i in range(idx, n):
                x = 10*x + ord(num[i]) - ord('0')
                str_x = str(x)
                if idx != 0:
                    dfs(num, i+1, path+'+'+str_x, ans, target, n, pre+val,  x)
                    dfs(num, i+1, path+'-'+str_x, ans, target, n, pre+val, -x)
                    dfs(num, i+1, path+'*'+str_x, ans, target, n, pre,  val*x)
                else:
                    dfs(num, i+1, str_x, ans, target, n, 0, x)
                if num[idx] == '0':
                    break
                    
        ans = []
        dfs(num, 0, '', ans, target, len(num), 0, 0)
        return ans
    
    
    
    
    
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        result, expr = [], []
        val, i = 0, 0
        val_str = ""
        while i < len(num):
            val = val * 10 + ord(num[i]) - ord('0')
            val_str += num[i]
            # Avoid "00...".
            if str(val) != val_str:
                break
            expr.append(val_str)
            self.addOperatorsDFS(num, target, i + 1, 0, val, expr, result)
            expr.pop()
            i += 1
        return result

    def addOperatorsDFS(self, num, target, pos, operand1, operand2, expr, result):
        if pos == len(num) and operand1 + operand2 == target:
            result.append("".join(expr))
        else:
            val, i = 0, pos
            val_str = ""
            while i < len(num):
                val = val * 10 + ord(num[i]) - ord('0')
                val_str += num[i]
                # Avoid "00...".
                if str(val) != val_str:
                    break
    
                # Case '+':
                expr.append("+" + val_str)
                self.addOperatorsDFS(num, target, i + 1, operand1 + operand2, val, expr, result)
                expr.pop()
    
                # Case '-':
                expr.append("-" + val_str)
                self.addOperatorsDFS(num, target, i + 1, operand1 + operand2, -val, expr, result)
                expr.pop()
        
                # Case '*':
                expr.append("*" + val_str)
                self.addOperatorsDFS(num, target, i + 1, operand1, operand2 * val, expr, result)
                expr.pop()
        
                i += 1
  
