#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/7/19 20:28
# @Author:JiahangGu
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        '''
        戳气球记分相邻气球的乘积，首先可以考虑在左右两侧分别加一个标记为1的气球，则
        问题转化为戳破左右边界气球之间的气球获得的最大值，这样可以省去边界判断的逻辑，
        然后一个气球戳完之后该气球的相邻气球变为相邻，这存在重复状态，例如[1,2,3,4]
        气球按照2314和3214的顺序戳都需要计算戳14的分数，所以如果可以提前知道14对应分
        数就可以避免重复计算，而[1,4]可以逆向考虑成向左右为1的气球之间加入气球的顺序
        得到的最大分数，对应的是与插入顺序逆序的戳破顺序，从而记录子状态的解。
        定义状态dp[i][j]表示气球i,j之间的气球戳破之后可以得到的最大分数，不包含ij即
        开区间
        初始化：dp[i][j]=0 if i+1 >= j,此时ij区间内无气球，因为要保证ij之间有气球，j-i>1
        解状态：dp[0][n-1]，这里的n是加入气球之后的长度
        状态转移：dp[i][j]=max(dp[i][j], dp[i][k]+dp[k][j]+nums[i]*nums[k]*nums[j])，因为
        dp[i][k]表示戳破ik之间气球剩下ik气球时的最大得分，dp[k][j]同理，所以此时剩下气球为
        ijk相邻，需要计算得到的最大分数，并且任一个气球都可能到达最优解，是一个区间dp。
        :param nums:
        :return:
        '''
        ball = [1] + nums + [1]
        n = len(ball)
        dp = [[0]*(n) for _ in range(n)]
        for i in range(n-2, -1, -1):
            for j in range(i+2, n):
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + ball[i] * ball[k] * ball[j])
        return dp[0][n-1]


x = [3,1,5,8]
s = Solution()
print(s.maxCoins(x))
