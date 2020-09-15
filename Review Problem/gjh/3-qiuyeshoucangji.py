#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/14 11:22
# @Author:JiahangGu


class Solution:
    def minimumOperations(self, leaves: str) -> int:
        """
        问题分解，按照ry出现的次数进行统计，并假设不连续的r、y的数目为列表a，b。如果len(a)>len(b)则表示
        ryryryr这种类型，即两边是r包住字串，这种情况一定是对rr中间的字符串进行转换；如果len(a)=len(b)，
        则表示ryryry或yryryr这种类型，可以将左边或右边的y全部转换为r或将边界的y转换为r，则得到第一种情况；
        如果len(a)<len(b)，则表示yryryry这种类型，可以将两边y全部转换或两边y的边界的一个y转换为r，得到第一
        种情况，继续求解。
        答案错误
        :param leaves:
        :return:
        """
        # def get_min_convert(numr, numy):
        #     if not nums_r:
        #         return 0
        #     if not nums_y:
        #         return 1
        #     return min(sum(numr), sum(numy)-max(numy))
        #
        # nums_r, nums_y = list(), list()
        # idx = 0
        # while idx < len(leaves):
        #     r_tmp = 0
        #     while idx < len(leaves) and leaves[idx] == 'r':
        #         r_tmp += 1
        #         idx += 1
        #     if r_tmp > 0:
        #         nums_r.append(r_tmp)
        #     y_tmp = 0
        #     while idx < len(leaves) and leaves[idx] == 'y':
        #         y_tmp += 1
        #         idx += 1
        #     if y_tmp > 0:
        #         nums_y.append(y_tmp)
        # if len(nums_r) > len(nums_y):
        #     if len(nums_r) == 1:
        #         return 1
        #     else:
        #         return get_min_convert(nums_r[1:-1], nums_y)
        # elif len(nums_r) == len(nums_y):
        #     if len(nums_r) == 1:
        #         return 1
        #     if leaves[0] == 'r':
        #         convert_right = nums_y[-1] + get_min_convert(nums_r[1:-1], nums_y[:-1])
        #         nums_y[-1] -= 1
        #         if nums_y[-1] == 0:
        #             nums_y.pop()
        #         convert_right1 = 1 + get_min_convert(nums_r[1:], nums_y)
        #         return min(convert_right1, convert_right)
        #     else:
        #         convert_left = nums_y[0] + get_min_convert(nums_r[1:-1], nums_y[1:])
        #         nums_y[0] -= 1
        #         if nums_y[0] == 0:
        #             nums_y.pop(0)
        #         convert_left1 = 1 + get_min_convert(nums_r[:-1], nums_y)
        #         return min(convert_left, convert_left1)
        # else:
        #     if len(nums_y) == 1:
        #         return 2
        #     if len(nums_r) == 1:
        #         nums_y[0] -= 1
        #         nums_y[-1] -= 1
        #         if nums_y[0] == 0:
        #             nums_y.pop(0)
        #         if nums_y[-1] == 0:
        #             nums_y.pop()
        #         return 2 + get_min_convert(nums_r, nums_y)
        #     convert_all = nums_y[0] + nums_y[-1] + get_min_convert(nums_r[1:-1], nums_y[1:-1])
        #     nums_y[0] -= 1
        #     nums_y[-1] -= 1
        #     if nums_y[0] == 0:
        #         nums_y.pop(0)
        #     if nums_y[-1] == 0:
        #         nums_y.pop()
        #     convert_all1 = 2 + get_min_convert(nums_r, nums_y)
        #     return min(convert_all, convert_all1)
        """
        此处记录看完题解之后的想法。首先是动态规划解法。因为要求两边必须是r，所以需要用到的状态有
        1.从左边开始全是r所需要的操作数，只需要从0开始遍历记录y的个数
        2.从左边开始前半部分是r，后半部分是y，这里的状态来自状态1或者状态2本身
        3.从左边开始前半部分是r，中间部分是y，后半部分是r，这里的状态来自状态2或状态3本身
        定义状态dp[0][i]表示状态1,dp[1][i]表示状态2，dp[2][i]表示状态3，则可以得到如下状态转移方程
        根据当前是r或者y判断
        if l[i] == 'r':
            dp[0][i] = dp[0][i-1]
            dp[1][i] = min(dp[0][i-1] + 1, dp[1][i-1] + 1)
            dp[2][i] = min(dp[1][i-1], dp[2][i-1])
        else:
            dp[0][i] = dp[0][i-1] + 1
            dp[1][i] = min(dp[0][i-1], dp[1][i-1])
            dp[2][i] = min(dp[1][i-1] + 1, dp[2][i-1] + 1)
        """
        # n = len(leaves)
        # dp = [[0] * n for _ in range(3)]
        # if leaves[0] == 'r':
        #     dp[0][0] = 0
        # else:
        #     dp[0][0] = 1
        # for i in range(1, n):
        #     if leaves[i] == 'r':
        #         dp[0][i] = dp[0][i-1]
        #     else:
        #         dp[0][i] = dp[0][i-1] + 1
        # if leaves[1] == 'r':
        #     dp[1][1] = dp[0][0] + 1
        # else:
        #     dp[1][1] = dp[0][0]
        # for i in range(2, n):
        #     if leaves[i] == 'r':
        #         dp[1][i] = min(dp[0][i - 1] + 1, dp[1][i - 1] + 1)
        #     else:
        #         dp[1][i] = min(dp[0][i-1], dp[1][i-1])
        # if leaves[2] == 'r':
        #     dp[2][2] = dp[1][1]
        # else:
        #     dp[2][2] = dp[1][1] + 1
        # for i in range(3, n):
        #     if leaves[i] == 'r':
        #         dp[2][i] = min(dp[1][i-1], dp[2][i-1])
        #     else:
        #         dp[2][i] = min(dp[1][i-1], dp[2][i-1]) + 1
        # return dp[2][n-1]
        """
        第二种思路，目的是要将字符串划分为特定的序列，假设序列为[0, n)，则目标序列划分为[0,i)，[i,j)和[j,n)，
        其中13部分为r，2部分为y。假设sum[i]表示从[0,i)中的红色的个数，则划分得到所需目标串的操作数为
        (i-sum[i]) + (sum[j]-sum[i]) + (n-j-(sum[n]-sum[j])，整理后得到n-sum[n] + (i-2*sum[i]) - (j - 2 * sum[j])
        ，即在满足0<i<j<n的条件下找到上式最小的值。
        此处注意变量的两项i-2*sum[i]和j-2*sum[j]的形式是一样的，且满足i<j，也就是在满足i<j的情况下遍历j得到最小的i-2*sum[i]即是
        最优解，而假设min[x]表示[1,x]区间内的i-2*sum[i]的最小值，i所属范围是[1,n-2]，则j遍历范围为[2,n-1]时，min[j-1]就表示
        当前最小的i-2*sum[i]。因为j只需要在当前j下最小的i-2*sum[i]，而对此前的i不关心。
        """
        n = len(leaves)
        sums = [0] * (n + 1)
        mins = [0] * n
        for i in range(1, n+1):
            sums[i] = sums[i-1] + (1 if leaves[i-1] == 'r' else 0)
        current_min = 1e9
        for i in range(1, n-1):
            current_min = min(current_min, i - 2 * sums[i])
            mins[i] = current_min
        ans = 1e9
        for j in range(n-1, 1, -1):
            ans = min(ans, n - sums[n] + mins[j-1] - j + 2 * sums[j])
        return ans


s = Solution()
print(s.minimumOperations("yyyrryyyrr"))
