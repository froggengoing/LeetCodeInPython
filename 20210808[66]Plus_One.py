# Given a non-empty array of decimal digits representing a non-negative integer,
#  increment one to the integer. 
# 
#  The digits are stored such that the most significant digit is at the head of 
# the list, and each element in the array contains a single digit. 
# 
#  You may assume the integer does not contain any leading zero, except the numb
# er 0 itself. 
# 
#  
#  Example 1: 
# 
#  
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
#  
# 
#  Example 2: 
# 
#  
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
#  
# 
#  Example 3: 
# 
#  
# Input: digits = [0]
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= digits.length <= 100 
#  0 <= digits[i] <= 9 
#  
#  Related Topics Array Math 
#  👍 2706 👎 3513


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        if digits[length - 1] != 9:
            res = digits
            res[length - 1] += 1
            return res
        max_res = [9] * length
        max_res[0] = digits[0]
        if max_res == digits:
            if max_res[0] == 9:
                res = [0] * (length + 1)
                res[0] = 1
            else:
                res = [0] * length
                res[0] = digits[0] + 1
            return res
        res = digits
        detal = 1
        for i in range(length - 1, 0, -1):
            tmp = res[i]
            res[i] = (detal + tmp) % 10
            detal = (detal + tmp) // 10
        return res

    def plusOne3(self, digits):
        numToStr = "".join([str(x) for x in digits])
        return [x for x in str(int(numToStr) + 1)]

    def plusOne2(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = 0
        for i in range(len(digits)):
            res += digits[i] * 10 ** (len(digits) - i - 1)
        return (res + 1)


# leetcode submit region end(Prohibit modification and deletion)
s1 = Solution()
print(s1.plusOne([1, 0, 1]))
