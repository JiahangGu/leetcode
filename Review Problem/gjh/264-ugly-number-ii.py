#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/22 17:19
# @Author:JiahangGu
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        求丑数的办法：因为质因数只有2,3,5所以记录一个使用2,3,5个数的索引，假设为num2,num3,num5.
        每次取出当前的最小丑数，并对比是2,3,5增加哪一个质因数得到的结果，将对应索引增加。
        :param n:
        :return:
        """
        num2, num3, num5 = 0, 0, 0
        nums = [1]
        n -= 1
        while n:
            num = min(nums[num2] * 2, nums[num3] * 3, nums[num5] * 5)
            nums.append(num)
            if num == nums[num2] * 2:
                num2 += 1
            if num == nums[num3] * 3:
                num3 += 1
            if num == nums[num5] * 5:
                num5 += 1
            n -= 1
        return nums[n - 1]


s = Solution()
print(s.nthUglyNumber(10))
