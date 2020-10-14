#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/14 13:42
# @Author:JiahangGu
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        遇到数字则入栈；遇到算符则取出栈顶两个数字进行计算，并将结果压入栈中。
        需要注意的是python的整除操作。例如-12/10得到-1.2，但是-12 // 10得到的是2，因为默认向下取整。
        所以需要使用int(-12/10)得到-1.
        :param tokens:
        :return:
        """
        stack = []
        for token in tokens:
            if token == '+':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num2)
            elif token == '-':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif token == '*':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 * num2)
            elif token == '/':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1 / num2))
            else:
                stack.append(int(token))
        return stack[0]


s = Solution()
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(s.evalRPN(tokens))
