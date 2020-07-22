#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/7/21 22:41
# @Author:JiahangGu


class Solution:
    def divisorGame(self, N: int) -> bool:
        '''
        Alice像获胜，只需要检验当前数字的所有因子，只要有一个为false
        则这个数字就可以获胜。因为数字只到1000也不需要做素筛。
        :param N:
        :return:
        '''
        # dp = [False] * (N+1)
        # dp[1] = False
        # for i in range(N+1):
        #     for j in range(1, i):
        #         if i % j == 0 and dp[i-j] == False:
        #             dp[i] = True
        #             break
        # return dp[N]
        '''
        通过dp的规律发现数组是True、False交替的，且数字为1时False，为2时True，可知如果能保证最终到达2
        就是True。考虑到奇数的因子都是奇数，在减去因子后得到偶数，而偶数的情况只需要每次减一变为奇数，
        对方必须减去因子又变回偶数，这样最终一定得到最小的偶数2。而如果初始为奇数，艾丽丝怎么样选都是
        变为偶数，进入上述的循环，必输。所以最终演变为对奇偶性的判断。
        '''
        return N % 2 == 0


s = Solution()
print(s.divisorGame(10))
