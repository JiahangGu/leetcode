#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/5 23:21
# @Author:JiahangGu
from typing import List


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        # def dfs(cur_city, left_fuel, path):
        #     nonlocal ans
        #     if left_fuel < 0:
        #         return
        #     if cur_city == finish:
        #         # print(path)
        #         ans = (ans + 1) % (10 ** 9 + 7)
        #     for i in range(0, len(locations)):
        #         if i != cur_city:
        #             path.append(i)
        #             dfs(i, left_fuel - abs(locations[i] - locations[cur_city]), path)
        #             path.pop()
        #
        # ans = 0
        # dfs(start, fuel, [start])
        # return ans
        """
        上述是超时的dfs解法，因为比赛过程中就发现这道题有大量的重复子结构，当时没有时间修改了（不熬夜）。
        重复子结构举例如下：从1出发到2，还剩k升汽油，那么这k升汽油在dfs过程中可以进入除2之外的任意一个点作为下一个点，而
        剩余k+abs(loc[1]-loc[2])升汽油的时候也面临这样的问题，而且路程是可以重复经过一个点的，这就意味着路程的长短由
        汽油的数量决定，在剩余同样的汽油量时路线可能有多种，那么在这个汽油量的基础上加上上一个站点过来花去的汽油，所得到的
        汽油量的结果其实应该是所有可以到达的点及所剩汽油的状态的方案数之和。
        假设dp[i][j]表示达到点i时消耗j升汽油可以得到的方案数，则dp[k][j+abs(loc[i]-loc[k])]+=dp[i][j]，即只要剩下
        的汽油可以到下一个点，那这个点的方案数就应该加上这个点的方案数。
        初始化：dp[start][fuel]不需要消耗汽油就可以到达，方案数为1.其余为0
        解：sum(dp[finish][f]) 0<=f<=fuel

        第二种表示方法：dp[i][j]表示到达点i时还剩j升汽油的方案数，则dp[k][j-abs(loc[i]-loc[j])]+=dp[i][j]
        :param locations:
        :param start:
        :param finish:
        :param fuel:
        :return:
        """
        n = len(locations)
        dp = [[0] * (fuel + 1) for _ in range(n)]
        dp[start][0] = 1
        ans = 0
        MOD = 10 ** 9 + 7
        for f in range(fuel+1):
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    x = f + abs(locations[i]-locations[j])
                    if x > fuel:
                        continue
                    dp[j][x] += dp[i][f]
                    dp[j][x] %= MOD
        for i in range(fuel+1):
            ans += dp[finish][i]
            ans %= MOD
        return ans


s = Solution()
print(s.countRoutes([80135,80136,80137,80138,80139,80140,80141,80142,80143,80144,80145,80146,80147,80148,80149,80150,80151,80152,80153,80154,80155,80156,80157,80158,80159,80160,80161,80162,80163,80164,80165,80166,80167,80168,80169,80170,80171,80172,80173,80174,80175,80176,80177,80178,80179,80180,80181,80182,80183,80184,80185,80186,80187,80188,80189,80190,80191,80192,80193,80194,80195,80196,80197,80198,80199,80200,80201,80202,80203,80204,80205,80206,80207,80208,80209,80210,80211,80212,80213,80214,80215,80216,80218,80219,80220,80221,80222,80223,80224,80225,80226,80227,80228,80229,80230,80231,80232,80233,80234,80235], 50, 50, 125))
