#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/16 11:51
# @Author:JiahangGu
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        """
        首先根据范围可知，从m循环到n可能超时。所以没有必要进行全循环。因为从m数到n的过程中，如果m二进制位数和n不同，则n的低m位都会是0，
        且n比m多的高位对m来说是0，所以也不会在结果中。而如果位数相同，则需要找m和n的最长公共前缀，因为这个前缀是在循环外的，不需要做与操作，
        所以始终不会变化。总结起来就是，寻找m和n的最长公共前缀。如果位数不同，认为m的高位都是0。所以只需要对m和n同时进行右移，直到二者相等，剩下
        的部分即为公共前缀。或者消除n中低位的1，因为高位中m默认为0.
        :param m:
        :param n:
        :return:
        """
        # shift = 0
        # while m < n:
        #     m = m >> 1
        #     n = n >> 1
        #     shift += 1
        # return m << shift
        while m < n:
            n = n & (n - 1)
        return n


s = Solution()
print(s.rangeBitwiseAnd(1, 3))
