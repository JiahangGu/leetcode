#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/6 10:40
# @Author:JiahangGu
from typing import List


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        square1 = []
        square2 = []
        from collections import defaultdict
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)
        for x in nums1:
            square1.append(x ** 2)
            freq1[x] += 1
        for x in nums2:
            square2.append(x ** 2)
            freq2[x] += 1
        ans = 0
        for x in square1:
            for j in nums2:
                if x % j == 0:
                    if x // j == j:
                        ans += max(0, freq2[j] - 1)
                    else:
                        ans += freq2[x // j]
        for x in square2:
            for j in nums1:
                if x % j == 0:
                    if x // j == j:
                        ans += max(0, freq1[j] - 1)
                    else:
                        ans += freq1[x // j]
        return ans // 2


s = Solution()
print(s.numTriplets([4,7,9,11,23], [3,5,1024,12,18]))
