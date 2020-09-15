#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/14 16:16
# @Author:JiahangGu
from typing import List


class Solution:
    def busRapidTransit(self, target: int, inc: int, dec: int, jump: List[int], cost: List[int]) -> int:
        """
        对问题进行拆分，首先到达一个点最快的方法是，通过jump尽量跳到接近target的地点，剩余的站点距离通过单站点移动补充。
        即跳到jump的倍数中满足jump*i<target<jump*(i+1)的i点，然后问题就转化为跳到i点所需的最小花销，如果恰好可以跳到target点则直接跳到即可
        。这样就形成了一个递归子问题，但由于到达每个点的花销可能是重复的子问题（对于不同jump），所以需要使用记忆化的方式，在这里使用
        字典实现。而对于jump数组则无法得知具体哪一跳会得到最优结果，且长度小于10，使用遍历即可。
        注意这里使用记忆化的方式，按照往常使用的记忆化方式在得到结果后为该key赋值的话在这里会导致无限递归，因为floor和floor+1可以会互相使用，
        例如求dfs(1)时会进入dfs(1)和dfs(0)，而dfs(1)还会继续进入导致一直卡在target=1的站点。可以使用提前赋值的方式，即给当前点赋一个大值，
        这个值不会影响结果（即小于ans，如1e18），则取出之后解决了递归循环问题也不影响最终结果。
        :param target:
        :param inc:
        :param dec:
        :param jump:
        :param cost:
        :return:
        """
        # def dfs(t):
        #     if t in cost_dict:
        #         return cost_dict[t]
        #     ans = t * inc
        #     cost_dict[t] = ans
        #     for i in range(len(jump)):
        #         if jump[i] == 1:
        #             continue
        #         if t % jump[i] == 0:
        #             ans = min(ans, dfs(t // jump[i]) + cost[i])
        #         else:
        #             floor = t // jump[i]
        #             ans = min(ans, dfs(floor) + cost[i] + (t - floor * jump[i]) * inc)
        #             ans = min(ans, dfs(floor+1) + cost[i] + ((floor+1) * jump[i] - t) * dec)
        #     cost_dict[t] = ans
        #     return ans
        #
        # cost_dict = dict()
        # cost_dict[0] = 0
        # ans = min(target * inc, dfs(target))
        # return ans % (10 ** 9 + 7)
        """
        这里尝试一下BFS的解法。解题思路如上，主要是用BFS实现优先队列，注意到题目要求找出最小花销，如果只是使用bfs无法确定最终是否可以得到
        最优解，因为可能在后续的0中出现的解是最优，但是因为flag中存在跳过，错过了最优解。如果使用优先队列，可以保证每次遍历的当前点是当前最优解，
        得到的第一个解也一定是最优解。
        """
        # stack保存目标点和到达所需的cost
        import heapq
        class Status:
            def __init__(self, p, t):
                self.pos = p
                self.cost = t

            def __lt__(self, other):
                return self.cost < other.cost

        heap = []
        heapq.heappush(heap, Status(target, 0))
        while True:
            x = heapq.heappop(heap)
            pos, cos = x.pos, x.cost
            if pos == 0:
                return cos % (10 ** 9 + 7)
            init_value = inc * pos
            heapq.heappush(heap, Status(0, cos + init_value))
            for i in range(len(jump)):
                floor = pos // jump[i]
                r = pos % jump[i]
                floor_cost = cost[i] + r * inc
                if floor_cost < init_value:
                    heapq.heappush(heap, Status(floor, cos + floor_cost))
                if r:
                    right_cost = (jump[i] - r) * dec + cost[i]
                    if right_cost < init_value:
                        heapq.heappush(heap, Status(floor+1, cos + right_cost))


s = Solution()
target = 31
inc = 5
dec = 3
jump = [6]
cost = [10]
print(s.busRapidTransit(target, inc, dec, jump, cost))
