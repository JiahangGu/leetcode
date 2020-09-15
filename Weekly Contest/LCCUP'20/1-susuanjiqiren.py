#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/14 10:59
# @Author:JiahangGu


class Solution:
    def calculate(self, s: str) -> int:
        """
        简单的模拟
        :param s:
        :return:
        """
        x = 1
        y = 0
        for i in range(len(s)):
            if s[i] == 'A':
                x = 2 * x + y
            elif s[i] == 'B':
                y = 2 * y + x
        return x + y


s = Solution()
print(s.calculate("AB"))
