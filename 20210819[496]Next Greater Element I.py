# The next greater element of some element x in an array is the first greater el
# ement that is to the right of x in the same array. 
# 
#  You are given two distinct 0-indexed integer arrays nums1 and nums2, where nu
# ms1 is a subset of nums2. 
# 
#  For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[
# j] and determine the next greater element of nums2[j] in nums2. If there is no n
# ext greater element, then the answer for this query is -1. 
# 
#  Return an array ans of length nums1.length such that ans[i] is the next great
# er element as described above. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so t
# he answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so t
# he answer is -1.
#  
# 
#  Example 2: 
# 
#  
# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
# - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so t
# he answer is -1.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums1.length <= nums2.length <= 1000 
#  0 <= nums1[i], nums2[i] <= 104 
#  All integers in nums1 and nums2 are unique. 
#  All the integers of nums1 also appear in nums2. 
#  
# 
#  
# Follow up: Could you find an O(nums1.length + nums2.length) solution? Related 
# Topics Array Hash Table Stack Monotonic Stack 
#  ð 432 ð 30


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def nextGreaterElement3(self, nums1, nums2):
        '''
        è¯è®ºç»åºçç­æ¡ï¼æ²¡æä½¿ç¨mapä¿å­ç»æãæ¶é´å¤æåº¦ä¸è¡
        :param nums1:
        :param nums2:
        :return:
        '''
        result = [-1] * len(nums1)
        stack = [0]
        for i in range(1, len(nums2)):
            while len(stack) != 0 and nums2[i] > nums2[stack[-1]]:
                if nums2[stack[-1]] in nums1:
                    # æ¶é´å¤æåº¦ä¸ºo(n)
                    index = nums1.index(nums2[stack[-1]])
                    result[index] = nums2[i]
                stack.pop()
            stack.append(i)
        return result

    def nextGreaterElement(self, nums1, nums2):
        '''
        ä½¿ç¨mapä¿å­nums[1]
        :param nums1:
        :param nums2:
        :return:
        ç±»ä¼¼é¢ç®ï¼åå³æ¾æå¤§å¼
        éånums2 å¾å°æ°å¼æ¯ä¸ªåç´ ä¸ä¸ä¸ªæå¤§å¼
        éånums1ï¼ç¸ç­åè·åå¯¹åºçä¸ä¸ä¸ªæå¤§å¼
        [1, 3, 4, 2]
        '''
        stack = []
        n2_dict = {}
        res = [-1] * len(nums1)
        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                cur = stack.pop()
                n2_dict[nums2[cur]] = nums2[i]
            stack.append(i)
        for i in range(len(nums1)):
            if nums1[i] in n2_dict:
                res[i] = n2_dict[nums1[i]]
        return res

    def nextGreaterElement1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        æ´åè§£æ³ï¼éånums1ï¼å¨éånums2
        """
        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            is_find = False
            for j in range(len(nums2)):
                if nums2[j] == nums1[i]:
                    is_find = True
                if is_find:
                    if nums2[j] > nums1[i]:
                        res[i] = nums2[j]
                        break
        return res


# leetcode submit region end(Prohibit modification and deleti
print(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
print(Solution().nextGreaterElement([2, 4], [1, 2, 3, 4]))
# a = {'2': 3, 'd': 5}
print(Solution().nextGreaterElement1([4, 1, 2], [1, 3, 4, 2]))
print(Solution().nextGreaterElement1([2, 4], [1, 2, 3, 4]))
