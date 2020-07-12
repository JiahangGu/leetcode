#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/7/8
# @Author:lulu


class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        使用二分法找到一个非负整数x的算术平方根，mid向上取整
        :param x:
        :return:
        '''
        left = 0
        right = x // 2 + 1 #这个算术平方根一定比x的二分之一要小，这里+1考虑x=1的情况
        while left < right:
            mid = left + (right - left + 1) // 2
            sqrt = mid * mid

            if sqrt > x:
                right = mid - 1
            else:
                left = mid

        return left


s = Solution()
ans = s.mySqrt(8)
print(ans)