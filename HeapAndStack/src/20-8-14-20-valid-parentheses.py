#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/4 15:51
# @Author:JiahangGu


class Solution:
    def isValid(self, s: str) -> bool:
        """
        栈的简单使用
        :param s:
        :return:
        """
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if not stack:
                    return False
                c = stack.pop()
                if char == ')':
                    if c != '(':
                        return False
                elif char == ']':
                    if c != '[':
                        return False
                elif char == '}':
                    if c != '{':
                        return False
        if stack:
            return False
        return True


s = Solution()
print(s.isValid("[]"))
