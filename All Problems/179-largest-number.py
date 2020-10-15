#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/15 9:40
# @Author:JiahangGu
from typing import List
from functools import cmp_to_key


def cmp(a, b):
    if a + b > b + a:
        return -1
    else:
        return 1


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        输出的排序结果是最大的整数，排序时将二者加起来返回更大的结果即可。
        :param nums:
        :return:
        """
        nums = [str(num) for num in nums]
        nums.sort(key=cmp_to_key(cmp))
        ans = ""
        for num in nums:
            ans += num
        idx = 0
        while idx < len(ans) - 1 and ans[idx] == '0':
            idx += 1
        return ans[idx:]


s = Solution()
print(s.largestNumber([0, 0]))
