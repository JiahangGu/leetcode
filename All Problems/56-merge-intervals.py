#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/4 16:43
# @Author:JiahangGu
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        对区间排序，然后遍历区间，记录待合并区间的LR，当前区间如果能和之前的区间合并，则更新待合并区间的范围，并继续遍历；
        如果不能更新，记录待合并区间到解空间，并更新待合并区间为当前区间
        :param intervals:
        :return:
        """

        def cmp(a, b):
            if a[0] == b[0]:
                if a[1] > b[1]:
                    return 1
                else:
                    return -1
            elif a[0] > b[0]:
                return 1
            else:
                return -1

        import functools
        if len(intervals) == 0:
            return []
        intervals.sort(key=functools.cmp_to_key(cmp))
        # print(intervals)
        ans = []
        res = intervals[0]
        for i in range(1, len(intervals)):
            # 不重叠，开始大于结束
            if intervals[i][0] > res[1]:
                ans.append(res)
                res = intervals[i]
            else:
                res[1] = max(res[1], intervals[i][1])
        ans.append(res)
        return ans
