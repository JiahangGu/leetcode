#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/4 15:52
# @Author:JiahangGu
from typing import List


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        """
        第一眼看起来是一个区间DP问题，定义状态dp[i][j]表示移除区间[i, j]能得到的最大积分，但在定义转移方程时出现了难点：
        按照dp[i][j]=dp[i][k]+dp[k][j]+operator(i,k,j)的公式来做，operator项似乎没有特殊含义，如果定义为ikj三个
        索引对应的元素是相同的，那在ik和kj内部可能仍存在相同元素，或者ij元素本来就不同。最根本的原因是：删除[i,j]区间之后
        可能得到新的更长的连续相同颜色序列，但也有可能由[i,j]区间内的数列删除部分构成更长的同色序列。所以子序列的结果不是独立
        的，而是由上一个序列删除的结果决定的，所以仅通过区间定义状态无法完全表示状态结果。
        解决方案：既然区间无法定义确切状态，那就把影响区间结果的所有可能因素都考虑进来，即区间后面所有元素中等于结尾元素的个数，
        因为当后面有相同元素时，在删除了这中间所有不同的元素之后可以构成一个更长的同色序列，而根据题意，连续序列越长得分越高，
        构成序列的长度由其后相同元素个数决定，所以可以定义状态dp[i][j][k]表示区间[i][j]且j后有k个与nums[j]同色的元素所能
        得到的最大积分。之所以这样定义，是因为nums[j]后有k个相同元素确定后，能得到的积分也就可以同样确定，因为最大长度是可知的。
        定义状态转移方程为dp[i][j][k] = max(dp[i][j-1][0] + (k+1）**2, dp[i][l][k+1] + dp[l+1][j-1][0]{i<l<j
         and nums[l]==nums[j]}),dp[i][j-1][0]+(k+1)**2表示先删除[i,j-1]再删除由j和其后的k个元素构成的长度为(k+1)的
         同色序列得到的积分，这里单独拿出来的原因是这个只移除左边的序列，而不删除[i,j]区间内的元素，并且假设左边除了与nums[j]
         同色的元素全部删掉。而后面的项表示nums[l]与nums[j]同色，那么可以删除(l,j)之间的所有项，从而由j以及j右边的k+1个数字
         构成的同色序列（这里有个疑问是，其实l和j相同，那可以直接得到长度为k+2的同色序列，即dp[i][j-1][k+2]，有待验证），这样
         就遍历到[i,j]内所有元素，得到所有可能结果中的最大值，从而保证这个状态转移是正确的。
         实现采用记忆化搜索的方式，因为k这个变量本身没有一个好的循环方式（可以从0-n），而使用记忆化搜索用到的k可以根据ij的状态直接初始化，
         并由ij直接决定k的遍历状态。（迭代推导也可以，但较麻烦）
        :param boxes:
        :return:
        """
        def max_value(l, r, k):
            if l > r:
                return 0
            if dp[l][r][k]:
                return dp[l][r][k]
            while r > l and boxes[r] == boxes[r-1]:
                r -= 1
                k += 1
            # 递推公式第一项，
            dp[l][r][k] = max_value(l, r-1, 0) + (k + 1) ** 2
            for i in range(l, r):
                # 递推第二项，相等时可以拼成更长的同色序列，有可能得到更大的解，而不同的时候不可能有更大解，可忽略
                if boxes[i] == boxes[r]:
                    dp[l][r][k] = max(dp[l][r][k], max_value(l, i, k+1) + max_value(i+1, r-1, 0))
            return dp[l][r][k]

        n = len(boxes)
        dp = [[[0] * n for _ in range(n)] for _ in range(n)]
        return max_value(0, n-1, 0)


s = Solution()
print(s.removeBoxes([1,2,1]))
