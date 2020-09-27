#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/27 17:08
# @Author:JiahangGu
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        目标是找最大矩形面积，最大面积由短边决定。如果暴力搜索，时间复杂度为O(n2)，因为每个点都要找后面的
        一条边。但其实最优解呈如下特点，假设矩形当前边为l, r，如果l移动或r移动之后长度变小，则面积只会不变或更小，
        且面积由短边决定，这就意味着如果能找到更大的最短边，就可以得到更大的面积。所以模拟两个边时，将更短的边移动到候选
        位置，才可能得到更优解，其余情况则无需考虑。且模拟过程中，由两边向中间收缩，宽越来越小，所以长度必须向更长的方向走.
        下述方法的一个优化点：既然要走向更长的地方，每次l或者r移动时，都找到能移动到的最长边，因为其中的短边都无法构成更优解。

        :param height:
        :return:
        """
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            ans = max(ans, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                for i in range(l+1, r):
                    if height[i] > height[l]:
                        l = i
                        break
            else:
                for i in range(r-1, l, -1):
                    if height[i] > height[r]:
                        r = i
                        break
        return ans


s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
