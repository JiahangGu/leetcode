#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/8/28 17:39
# @Author:JiahangGu

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        """
        根据数据范围可知暴力求解会超时，那么一定不需要遍历整个范围。根据与操作的特点可知，若某一位存在0则结果中该位也是0，
        在将mn转化为2进制后，如果位数不同则结果为0，因为从m到n必须经历首位为1其余为0的数字，这样就导致结果为0.而同位时，
        差值对应的2进制位数范围的所有位都会覆盖到0，即如果m=5, n=7，则m=[1,0,1],n=[1,1,1]，差值为3=[0,1,0]，会从
        除第一位外都会出现0.所以结果是[1,0,0]=4。即要找到mn转化为2进制串后的公共前缀
        :param m:
        :param n:
        :return:
        """
        # def bit_convert(x):
        #     ans = []
        #     while x:
        #         ans.append(x % 2)
        #         x //= 2
        #     return ans[::-1]
        #
        # if m == n:
        #     return m
        # m_bits = bit_convert(m)
        # n_bits = bit_convert(n)
        # diff_bits = bit_convert(n-m)
        # if len(m_bits) != len(n_bits):
        #     return 0
        # else:
        #     i = 0
        #     ans = 0
        #     while m_bits[i] == n_bits[i] and i < len(m_bits) - len(diff_bits):
        #         ans += pow(2, len(m_bits)-i-1) * m_bits[i]
        #         i += 1
        # return ans
        """
        官方题解：如上所述，主要问题在于找到公共前缀，则通过移位操作直到第一个相等的进制位。
        """
        # shift = 0
        # while m < n:
        #     m = m >> 1
        #     n = n >> 1
        #     shift += 1
        # return m << shift
        """
        Brian Kernighan算法：用于清除二进制串中最右边的1.关键思路在于每次对n和n-1进行按位与运算后，n最右边的1会变为0.
        """
        while m < n:
            n = n & (n - 1)
        return n


s = Solution()
print(s.rangeBitwiseAnd(4, 5))
