#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/21 15:40
# @Author:JiahangGu
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        普通，首先求出前缀乘积和后缀乘积。
        求i只需要拿出前缀后缀相乘
        '''
        # pre, post = nums.copy(), nums.copy()
        # for i in range(1, len(nums)):
        #     pre[i] *= pre[i-1]
        # for i in range(len(nums)-2, -1, -1):
        #     post[i] *= post[i+1]
        # ans = []
        # ans.append(post[1])
        # for i in range(1, len(nums)-1):
        #     ans.append(pre[i-1]*post[i+1])
        # ans.append(pre[len(nums)-2])
        # return ans
        '''
        进阶。因为输出数组不算入空间复杂度，所以用输出数组计算前缀乘积，然后维护一个数字记录后缀乘积，更新结果。
        '''
        ans = nums.copy()
        for i in range(1, len(nums)):
            ans[i] *= ans[i-1]
        ans[-1] = ans[-2]
        post = nums[-1]
        for i in range(len(nums)-2, 0, -1):
            ans[i] = ans[i-1] * post
            post *= nums[i]
        ans[0] = post
        return ans
