# Time:  O(logn), n is the value of the integer
# Space: O(1)
#
# Convert a non-negative integer to its english words representation.
# Given input is guaranteed to be less than 2^31 - 1.
#
# For example,
# 123 -> "One Hundred Twenty Three"
# 12345 -> "Twelve Thousand Three Hundred Forty Five"
# 1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
#
# Hint:
#
# 1. Did you see a pattern in dividing the number into chunk of words?
# For example, 123 and 123000.
#
# 2. Group the number by thousands (3 digits). You can write a helper
# function that takes a number less than 1000 and convert just that chunk to words.
#
# 3. There are many edge cases. What are some good test cases?
# Does your code work with input such as 0? Or 1000010?
# (middle chunk is zero and should not be printed out)
#

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"

        lookup = {0: "Zero", 1:"One", 2: "Two", 3: "Three", 4: "Four", \
                  5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", \
                  10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", \
                  15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", \
                  20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", \
                  70: "Seventy", 80: "Eighty", 90: "Ninety"}
        unit = ["", "Thousand", "Million", "Billion"]

        res, i = [], 0
        while num:
            cur = num % 1000
            if num % 1000:
                res.append(self.threeDigits(cur, lookup, unit[i]))
            num //= 1000
            i += 1
        return " ".join(res[::-1])

    def threeDigits(self, num, lookup, unit):
        res = []
        if num / 100:
            res = [lookup[num / 100] + " " + "Hundred"]
        if num % 100:
            res.append(self.twoDigits(num % 100, lookup))
        if unit != "":
            res.append(unit)
        return " ".join(res)
    
    def twoDigits(self, num, lookup):
        if num in lookup:
            return lookup[num]
        return lookup[(num / 10) * 10] + " " + lookup[num % 10]
    
    
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        
        neg = "Negative" if num < 0 else ""
        
        unit = ["", "Thousand", "Million", "Billion"]
        
        lookup = {1:"One", 2: "Two", 3: "Three", 4: "Four", \
                  5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", \
                  10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", \
                  15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", \
                  20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", \
                  70: "Seventy", 80: "Eighty", 90: "Ninety"}
        
        def do_three(num, lookup):
            result = []
            if num >= 100:
                result.append(lookup[num/100])
                result.append("Hundred")
            
            if num % 100 != 0:
                if 0 < (num % 100) < 20:
                    result.append(lookup[num % 100])
                else:
                    num = num % 100
                    result.append(lookup[(num % 100) - (num % 10)])

                    if 0 < (num % 10) < 10:
                        result.append(lookup[num % 10])
            
            return ' '.join(result)
        
        
        result = []
        
        ut = 0
        while num > 0:
            last_three = num % 1000
            num_str = do_three(last_three, lookup)
            if num_str != '':
                if ut > 0:
                    result.append(unit[ut])
                result.append(num_str)
            ut += 1
            num /= 1000
            
        return neg + ' '.join(result[::-1])
