#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/6 16:59
# @Author:JiahangGu
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        首先判断总油量是否够走一圈，如果不可以的话说明怎么走也无法行驶一周，返回-1，
        这里的贪心思路一开始是正确的，但是不会证明，证明过程参考题解。
        解法：从0出发，一路走到尾并沿途计算gas和cost的差值，并计算行驶过程中油箱最小的值min，如果为负就表明需要提前准备min油。
        如果最终的min大于0，那么可以从0点出发走一圈，如果小于0，则表明0不能，并且已知到达某个点需要最多的油(min记录)，则从最后
        一个点开始向前遍历，如果当前已有的油量可以到达需要油最多的那个点，则该点可以作为出发点。
        证明：假设min对应的为k点，那么0-k需要至少min油，从右向左遍历时，如果某点可以满足剩余总油量+min>0，那么从这个点开始，首先
        走到最右点，剩余油量>min,而0-k只需要min，可以走完。
        类似的解法还有，从0开始遍历寻找最大剩余油量的位置，找到最大值后向左搜索，首先找到第一个小于0的位置，表明从这里走不完一圈，
        但可能从他之前走可以走一圈，然后设定当前油量为0，向左搜索，找到最后一个满足加上该点后剩余油量大于等于0的位置，则该位置是起点
        :param gas:
        :param cost:
        :return:
        """
        # summ = 0
        # minn = 0
        # n = len(gas)
        # for i in range(n):
        #     summ += gas[i] - cost[i]
        #     minn = min(minn, summ)
        # if summ < 0:
        #     return -1
        # if minn >= 0:
        #     return 0
        # for i in range(n-1, -1, -1):
        #     minn += gas[i] - cost[i]
        #     if minn >= 0:
        #         return i
        # return -1
        """
        另一种贪心算法的思路是，如果总油量大于总消耗，那么一定存在一个解。并且基于如下发现，如果A无法到B，即剩余油量<0，
        则说明A到B之间的所有站点，均不能作为起始点，所以可能的站点是下一个站点。
        """
        summ = 0
        cur_gas = 0
        idx = -1
        for i in range(len(gas)):
            summ += gas[i] - cost[i]
            cur_gas += gas[i] - cost[i]
            if cur_gas < 0:
                idx = i
                cur_gas = 0
        if summ < 0:
            return -1
        return (idx + 1) % len(gas)


s = Solution()
gas  = [1,2,3,4,5]
cost = [3,4,5,4,2]
print(s.canCompleteCircuit(gas, cost))
