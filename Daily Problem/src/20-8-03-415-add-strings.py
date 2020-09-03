#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/3 16:23
# @Author:JiahangGu


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """
        字符串相加，从末尾开始比较，如果有进位则继续前移，直到没有进位将更长的数字字符串补充到前面的位置。
        :param num1:
        :param num2:
        :return:
        """
        # if not num1:
        #     return num2
        # if not num2:
        #     return num1
        # l1 = len(num1)
        # l2 = len(num2)
        # ans = []
        # if l2 > l1:
        #     num1, num2 = num2, num1
        #     l2, l1 = l1, l2
        # pos1, pos2 = l1 - 1, l2 - 1
        # c = 0
        # while pos1 >= 0 and pos2 >= 0:
        #     x1 = num1[pos1]
        #     x2 = num2[pos2]
        #     s = int(x1) + int(x2) + c
        #     c = s // 10
        #     ans.append(str(s % 10))
        #     pos1 -= 1
        #     pos2 -= 1
        # while c and pos1 >= 0:
        #     s = int(num1[pos1]) + c
        #     ans.append(str(s % 10))
        #     c = s // 10
        #     pos1 -= 1
        # while pos1 >= 0:
        #     ans.append(num1[pos1])
        #     pos1 -= 1
        # if c:
        #     ans.append("1")
        # return "".join(ans[::-1])
        """
        精简版，上述代码行数多，因为首先指定num1大于num2，然后在num1和num2都有数值的地方相加，在num2遍历完之后对num1单独处理
        看num1是否有进位没有加完，进位加完之后要把num1原始的字符加入到结果中，这种按照阶段流程完成的情况导致代码复杂但逻辑清晰。
        这里参考官方题解，在位数较短时即下标处于负数时返回0，等于对较短的数字串进行了补零操作，可以除去两个数字位数不同的情况。
        """
        l1, l2, c = len(num1)-1, len(num2)-1, 0
        ans = []
        while l1 >= 0 or l2 >= 0 or c:
            x1 = int(num1[l1]) if l1 >= 0 else 0
            x2 = int(num2[l2]) if l2 >= 0 else 0
            s = x1 + x2 + c
            ans.append(str(s % 10))
            c = s // 10
            l1 -= 1
            l2 -= 1
        return "".join(ans[::-1])


s = Solution()
print(s.addStrings("999999", "1"))
