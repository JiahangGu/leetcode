#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/20 18:19
# @Author:JiahangGu
class Solution:
    def calculate(self, s: str) -> int:
        """
        栈模拟即可，期间去掉所有空格。一个栈存储数字，一个栈存储运算符，如果是乘除法则先计算出结果再放入栈，
        然后取出两个数字和一个运算符计算结果。
        :param s:
        :return:
        """
        def is_digit(c):
            return '0' <= c <= '9'

        stack = []
        sign = "+"
        num = 0
        for i in range(len(s)):
            if is_digit(s[i]):
                num = num * 10 + int(s[i])
            if (not is_digit(s[i]) and s[i] != ' ') or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    pre = stack.pop()
                    stack.append(num * pre)
                elif sign == '/':
                    pre = stack.pop()
                    stack.append(int(pre / num))
                sign = s[i]
                num = 0
        return sum(stack)


s = Solution()
print(s.calculate(" 3+ 2* 2"))