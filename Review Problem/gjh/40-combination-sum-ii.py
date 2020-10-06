#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/10 20:18
# @Author:JiahangGu
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        和前一天的组合题的区别在于，前一天可以无限使用，理论上按理说是没有重复解的，因为一个数字重复的次数是递归决定的。
        而现在要求不能重复则是包含了重复的相同元素，比如[1,2,2,2]在target=5时会出现三次122的组合。解决的办法有两种
        1.是判断当前元素是否和前一个相同并且不是当前递归的元素位置，如果相同则没有必要进入，因为在前一层递归已经统计到了，
        而如果是当前递归元素，则需要进入深层递归，因为此前已经将相同的后续元素过滤，此时进入递归才可以补充所缺失的情况，例如
        [1,2,2,2]如果不判断递归层，则后续的两个2都进不去，导致情况缺失，如果是递归层则进入深层从下一个元素开始
        :param candidates:
        :param target:
        :return:
        """
        # def dfs(pos, left, path):
        #     if left == 0:
        #         ans.append(path[:])
        #     if left < 0:
        #         return
        #     for i in range(pos, len(candidates)):
        #         # 如果不是当前递归层并且和前一个元素一样，则不需要进入深层递归
        #         if i - 1 >= pos and candidates[i] == candidates[i-1]:
        #             continue
        #         path.append(candidates[i])
        #         dfs(i+1, left-candidates[i], path)
        #         path.pop()
        #
        # ans = []
        # candidates.sort()
        # dfs(0, target, [])
        # return ans
        """
        解法2是统计数组中每个元素出现的次数，并在递归时根据当前剩余值和该元素的总个数决定应该进入多少次递归。
        解法3是在统计结果处做hash映射判断结果是否在ans中出现从而去重，不再实现，思路是利用Rabin-Karp算法求hash。
        """
        def dfs(pos, left, path):
            if left == 0:
                ans.append(path[:])
                return
            if pos >= len(freq) or left < freq[pos][0]:
                return
            # 不使用当前元素
            dfs(pos+1, left, path)
            most = min(left // freq[pos][0], freq[pos][1])
            # 将当前元素可以放入的次数分别遍历一次
            for i in range(1, most+1):
                path.append(freq[pos][0])
                dfs(pos+1, left-i*freq[pos][0], path)
            # 将上面的循环放入的元素弹出，恢复原状
            for i in range(most):
                path.pop()

        from collections import Counter
        freq = sorted(Counter(candidates).items())
        ans = []
        dfs(0, target, [])
        return ans


s = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
print(s.combinationSum2(candidates, target))
