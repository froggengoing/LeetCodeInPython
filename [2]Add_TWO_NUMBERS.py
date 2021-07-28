class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first = ListNode()
        t1 = l1
        t2 = l2
        node = first
        while True:
            # python 的三目运算
            v1 = t1.val if t1 is not None else 0
            v2 = t2.val if t2 is not None else 0
            cur = (v1 + v2 + node.val) % 10
            next = (v1 + v2 + node.val) // 10
            node.val = cur
            t1 = None if t1 is None else t1.next
            t2 = None if t2 is None else t2.next
            if t1 is None and t2 is None:
                if next > 0:
                    node.next = ListNode(next)
                break
            node.next = ListNode(next)
            node = node.next
        return first

    # leetcode submit region end(Prohibit modification and deletion)
    def addTwoNumbers2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        [2,4,3] + [5,6,4] = [7,0,8]
        """
        # 如果a>b的结果为真，h="变量1",如果为假，h="变量2"
        # h = "变量1" if a>b else "变量2"
        length1 = len(l1)
        length2 = len(l2)
        # Range范围是[0,max)，所以不能减一
        # max_index = length1 - 1 if length1 > length2 else length2 - 1
        max_index = length1 if length1 > length2 else length2
        remainder = 0
        cur1 = 0
        cur2 = 0
        res = []
        for index in range(max_index):
            if index < length1:
                cur1 = l1[index]
            if index < length2:
                cur2 = l2[index]
            value = (cur1 + cur2 + remainder) % 10
            remainder = (cur1 + cur2 + remainder) // 10
            # 报错，list使用append追加元素
            # res[index] = value
            res.append(value)
            cur1 = 0
            cur2 = 0
        if remainder > 0:
            # res[max_index + 1] = remainder
            res.append(remainder)
        return res


def parse(n1):
    if len(n1) >= 1:
        node = ListNode(n1[0])
        cir_node = node
        for value in range(1, len(n1)):
            cir_node.next = ListNode(n1[value])
            cir_node = cir_node.next
        return node
    return None


s1 = Solution()
# # print(s1.addTwoNumbers([2, 4, 3], [5, 6, 4]))
# print(s1.addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
v1 = parse([9, 9, 9, 9, 9, 9, 9])
v2 = parse([9, 9, 9, 9])
l3 = s1.addTwoNumbers(v1, v2)
print(l3)
