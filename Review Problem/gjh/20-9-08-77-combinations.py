#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/8 11:07
# @Author:JiahangGu
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        遍历(1~n-k+1)，并记录当前组合序列，长度达到k记录。
        注意回溯过程中会有很多无意义的递归，比如剩余元素全部加上也凑不够k位时需要剪枝，而实际上这种情况很多
        剪枝后运行时间由604ms减少到64ms
        :param n:
        :param k:
        :return:
        """
        # def back_track(path, cur):
        #     if cur > k and len(path) == k:
        #         ans.append(path[:])
        #         return
        #     # 剪枝，即剩余所有元素都加上也凑不够k位
        #     if len(path) + (n - cur + 1) < k:
        #         return
        #     for i in range(cur, n+1):
        #         path.append(i)
        #         back_track(path, i+1)
        #         path.pop()
        #
        # ans = []
        # back_track([], 1)
        # return ans
        """
        回溯算法解决这个问题过于简单，可以尝试更有挑战性的迭代方法。
        要组合的是1-k个数字，可以想到如果使用n位二进制表示每一个组合，则每个组合对应的二进制都是不同的。
        二进制数字找下一个排列的方法相比于在组合方面要更简单。例如1010的next组合是1100，101100的下一个组合是110001，
        可以看出，next序列相比于当前二进制数字来说，最右侧的连续1子序列中最左边的1和1左边的0换了位置，并且将这个1右边的所有
        1都移动到低位。
        根据末尾是否为1分为两种情况：
        1.最低位为1，且假设末尾有t个连续的1，直接将倒数第t位的1和倒数第t+1位的0替换就得到了next(x)
        2.最低位为0，假设末尾有t个连续的0，然后接m个连续的1.则将倒数第t+m位置的1和倒数第t+m+1位置的0互换，然后把倒数第t+1
        位到倒数第t+m-1位的1移动到最低位。第一种情况可以看作t=0的特殊情况。
        而对应到组合来看，假设a=[a0,a1...ak]表示k个数字的组合并且a0对应二进制的低位，如果ai存在，
        则表示ai对应的二进制位置为1，否则为0。对于上述寻找连续1的解法，可以转换成寻找第一个不满足aj+1==a(j+1）的数字，不等
        时这两个数字之间一定存在0，此时可以将aj的数字+1，对应于将最左边的1和1左边的0互换位置，而在寻找这个数字的过程中，将
        [0, t-1]的区间赋值为[1, t]，对应的是将1右边的所有1都移动到低位。整个过程对应二进制的转换就相当于，有连续t个1，将
        [0. t-1]的区间赋值为1，而将第t个1放到t+1的位置。
        """
        tmp = [i for i in range(1, k+1)]
        # 第一种解是[1,k]
        tmp.append(n+1)
        ans = []
        j = 0
        # 构造解只需要得到k位即可，并且结束条件是得到解[n-k+1, n]
        while j < k:
            # 最后一位标志位不需要加到解
            ans.append(tmp[:k])
            # 找到第一个不满足的点，并且重置遍历过的区域
            j = 0
            while j < k and tmp[j] + 1 == tmp[j+1]:
                tmp[j] = j + 1
                j += 1
            # 第一个不满足的点左移一位，对应在组合情况就是数字+1
            tmp[j] += 1
        return ans


s = Solution()
print(s.combine(4, 2))
