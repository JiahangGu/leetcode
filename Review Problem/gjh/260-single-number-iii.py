#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/22 16:50
# @Author:JiahangGu
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        本题要求使用常数空间，且其余元素出现两次，可以想到需要用到位运算中的异或，异或操作可以去除所有出现次数为偶数次的数字。
        但由于有两个数字不同，最终结果是两个不同数字的异或结果。基于异或结果是不同的为1，则最终异或结果中为1的位与两个不同的数字
        求异或的结果是不同的，可以以此区分。所以求出整个数组异或结果后，找出任意一位为1的位，再进行一次遍历，按照该位异或结果
        为0或1拆分为两个数组，且这两个数组各自的异或结果就是最终不同的两个数字。
        :param nums:
        :return:
        """
        res = 0
        for num in nums:
            res = res ^ num
        flag = 1
        while not res & flag:
            flag <<= 1
        one, two = 0, 0
        for num in nums:
            if num & flag:
                one = one ^ num
            else:
                two = two ^ num
        return [one, two]


s = Solution()
nums = [1,2,1,3,2,5]
print(s.singleNumber(nums))
