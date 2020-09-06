#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/5 22:59
# @Author:JiahangGu
from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        """
        比赛时想到的解法：找到左右两边的最长非递减序列，然后从边界中找到要删除的位置，但是存在的问题是从一个位置开始如何判断
        要删除到哪个位置结束。
        看完题解后明白：找到删除的位置不一定要删除，首先最长的非递减序列是找到的左右序列拼接起来的，如果左边最大小于等于右边
        最小的话，主要是这一点，因为这就可以确定在删除的时候，得到的结果一定是小于等于这个结果的，那就可以忽略中间的数组序列，
        只看这两个序列拼接起的最长非递减序列长度，而这很好求。对于左边每一个位置，找到右边第一个大于等于的位置即可，
        :param arr:
        :return:
        """
        n = len(arr)
        l, r = 0, n - 1
        while l < n - 1 and arr[l] <= arr[l+1]:
            l += 1
        # 本身就是非递减序列
        if l + 1 == n:
            return 0
        while r >= 1 and arr[r-1] <= arr[r]:
            r -= 1
        # 从右边序列长度开始，将左边非递减序列加到右边，求最长非递减序列长度，从左边开始，将右边加入也同样可以
        ans = n - r
        # 注意，这里添加一个很大的数（上界），表示最右边的元素本身可以构成一个长度为1的非递减序列
        arr.append(1e9)
        r = n
        for i in range(l, -1, -1):
            while arr[i] <= arr[r-1] <= arr[r] and r - 1 > i:
                r -= 1
            ans = max(ans, i + 1 + n - r)
        return n - ans


s = Solution()
print(s.findLengthOfShortestSubarray([6,11,20,20,7,22,22,22,6,4,9]))
