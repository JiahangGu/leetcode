#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/22 16:09
# @Author:JiahangGu
from typing import List


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        """
        首先，对于一个运算式来说，任意运算符都有可能最后一个运算，而最后一个运算的顺序不同也就决定了不同的
        结果。假设有n个运算符，则选定一个为最终运算位假设为k，则前k-1个运算符和后n-k-1位运算符得到的结果
        可以使用当前运算符拼接。显而易见这是一个分治策略。
        最初拆分时按照每个运算符求解剩余两边运算符的结果，然后将两边结果按照剩余运算符合并，合并是O(n^2)复杂度
        :param input:
        :return:
        """
        def is_digit(c):
            return '0' <= c <= '9'

        def devide(nums, operators):
            if len(nums) == 1:
                return nums
            res = []
            for i in range(len(operators)):
                pre = devide(nums[:i+1], operators[:i])
                post = devide(nums[i+1:], operators[i+1:])
                if operators[i] == '+':
                    for num in pre:
                        for num2 in post:
                            res.append(num + num2)
                elif operators[i] == '-':
                    for num in pre:
                        for num2 in post:
                            res.append(num - num2)
                elif operators[i] == '*':
                    for num in pre:
                        for num2 in post:
                            res.append(num * num2)
            return res

        num = 0
        num_list = []
        operator_list = []
        for i in range(len(input)):
            if is_digit(input[i]):
                num = num * 10 + int(input[i])
            else:
                num_list.append(num)
                num = 0
                operator_list.append(input[i])
        num_list.append(num)
        return devide(num_list, operator_list)


s = Solution()
print(s.diffWaysToCompute("11*2-3"))
