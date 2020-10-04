#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/4 15:33
# @Author:JiahangGu
class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        快速幂考察，复习一下。
        首先使用1作为起始点，如果当前幂次为奇数，首先乘一个x，然后x=x*x作为下一次乘法基准。因为最后总会有n==1的情况，此时
        将ans赋予正确的解。
        对于2^7来说，先求ans=2,x=4,n=3,然后ans=8,x=16,n=1,最后ans=128结束。相当于中间使用x来记录当前已经出现过的偶数
        幂次的结果，而奇数幂次则直接加到ans中，不反应在x上。这样符合x^7=x^3 * x^3 * x的公式，ans首先乘最后一个x，其次
        才是计算x^3，并且此时x^3也是一个子问题。
        递归解法很简单，
        if n == 1: return x
        y = dfs(x, n // 2)
        return y * y if n & 1 else y * y * x
        :param x:
        :param n:
        :return:
        """
        if x == 0:
            return 0
        if n == 0:
            return 1
        flag = 1
        if n < 0:
            flag = -1
            n = -n
        ans = 1.0
        while n:
            if n & 1:
                ans *= x
            x *= x
            n //= 2
        if flag < 0:
            return 1.0 / ans
        return ans


s = Solution()
print(s.myPow(8.84372, -5))
