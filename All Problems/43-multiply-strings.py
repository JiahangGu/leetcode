#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/4 15:51
# @Author:JiahangGu


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        从后往前遍历num1的单个数字字符与num2做乘法，倒数第i位的num1要先补i-1个0到数组，然后记录乘法结果，最终进行
        大数的字符串加法
        :param num1:
        :param num2:
        :return:
        """
        def add_string(n1, n2):
            l1, l2, c = len(n1) - 1, len(n2) - 1, 0
            ans = []
            while l1 >= 0 or l2 >= 0 or c:
                x1 = int(n1[l1]) if l1 >= 0 else 0
                x2 = int(n2[l2]) if l2 >= 0 else 0
                s = x1 + x2 + c
                ans.append(str(s % 10))
                c = s // 10
                l1 -= 1
                l2 -= 1
            return ans[::-1]

        def multiply(char, num, last0):
            ans = ["0"] * last0
            l = len(num) - 1
            x = int(char)
            c = 0
            while l >= 0:
                z = int(num[l]) * x + c
                c = z // 10
                ans.append(str(z % 10))
                l -= 1
            if c != 0:
                ans.append(str(c))
            return ans[::-1]

        if num1[0] == '0' or num2[0] == '0':
            return '0'
        res = multiply(num1[-1], num2, 0)
        n = len(num1)
        for i in range(1, n):
            tmp = multiply(num1[n-i-1], num2, i)
            res = add_string(tmp, res)
        return "".join(res)


s = Solution()
print(s.multiply("0", "456"))
