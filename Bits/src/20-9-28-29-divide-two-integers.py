#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/27 23:04
# @Author:JiahangGu
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        可以使用移位操作实现乘除法，但每次只能乘除2的倍数。可以先用lgn复杂度确定区间，然后递减搜索到第一个
        小于dividend的次数。但是会超时，因为确定的区间可能很大，每次循环只减divisor导致循环次数太大。
        可以首先记录divisor的2的倍数放入列表中，然后每次找到最大的小于dividend的值，记录索引作为倍数，更新dividend为
        减去找到的值，直到最终索引为0.注意对结果中边界条件的处理。此外还有dividend<=divisor的特殊情况，通过倍数list的长度可以得知
        :param dividend:
        :param divisor:
        :return:
        """
        def binary_search(target):
            l, r = 0, len(multi) - 1
            if multi[l] > target:
                return -1
            while l < r:
                mid = l + (r - l + 1) // 2
                if multi[mid] > target:
                    r = mid - 1
                else:
                    l = mid
            return l

        if dividend == 0:
            return 0
        flag = 1
        if (divisor > 0 and dividend < 0) or (divisor < 0 and dividend > 0):
            flag = -1
        divisor = abs(divisor)
        x = divisor
        dividend = abs(dividend)
        multi = []
        while x <= dividend:
            multi.append(x)
            x <<= 1
        ans = 0
        if len(multi) == 0:
            return 0
        while True:
            idx = binary_search(dividend)
            if idx == -1:
                break
            ans += 1 << idx
            dividend -= multi[idx]
        if flag == 1:
            if ans > 2 ** 31 - 1:
                return 2 ** 31 - 1
            else:
                return ans
        else:
            if -ans < -2 ** 31:
                return -2 ** 31
            else:
                return -ans


s = Solution()
print(s.divide(10, -3))
