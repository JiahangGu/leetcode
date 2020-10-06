#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/4 15:56
# @Author:JiahangGu
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        使用一个数组标记当前可以到达的所有位置，对于每个位置，标记能跳到的点之间所有点为可达，并使用一个ans记录当前到达的最大位置。
        每个位置都可能跳到最后一个位置之前的位置，要对所有中间的点标记，复杂度为O(N^2)。
        :param nums:
        :return:
        """
        # ans = 0
        # flag = [0] * len(nums)
        # flag[0] = 1
        # for i in range(len(nums)):
        #     if flag[i] == 0:
        #         continue
        #     ans = max(ans, i + nums[i])
        #     if ans >= len(nums):
        #         return True
        #     for j in range(i+1, nums[i] + i + 1):
        #         flag[j] = 1
        # return False
        """
        上述解法在极限情况超时（n<=25000)，n2肯定超。考虑做一个优化，上述问题卡在了对所有能到位置的标记过程。
        跳跃过程中，唯一能限制到无法继续向前跳跃的条件是，能跳到的最大位置处可以跳跃0，而在这之前的0其实都可以无视，
        因为已经可以到达。所以只需要在等于0的时候判定一下是否是当前能到的最大位置，如果不是就可以继续向前，如果是则返回False.
        或者说记录一个能到达的最大位置，如果当前位置是大于最大位置的，那么说明该位置无效，返回False.
        这种解法是隐式BFS，因为其实也是类似BFS记录能到达的所有点然后取出点继续放入所有可到的点集合的解法。只不过这里的BFS只需要
        记录可到达的最大点，而不是记录所有可到达的点。
        """
        ans = 0
        for i in range(len(nums)):
            if i > ans:
                return False
            ans = max(ans, i + nums[i])
            if ans >= len(nums) - 1:
                return True
        return True


s = Solution()
print(s.canJump([0]))
