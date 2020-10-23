#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/23 9:15
# @Author:JiahangGu
class Solution:
    def numSquares(self, n: int) -> int:
        """
        贪心法来每次选择当前小于n的最大平方数时容易陷入局部最优解，例如12=4+4+4
        然后发现这个是具有重复子结构的，比如13的个数由4和9的个数决定。假设dp[i]表示i对应的个数，则dp[i] = min(dp[k], dp[i-k])，
        并且dp[i]的状态更新只有在k是平方数的时候才进行，所以只需要对小于n的平方数遍历即可。时间复杂度为O(n^1.5)
        :param n:
        :return:
        """
        # from math import sqrt
        # dp = [10000] * (n + 1)
        # square = set()
        # for i in range(1, int(sqrt(n)) + 1):
        #     x = i * i
        #     dp[x] = 1
        #     square.add(x)
        # for i in range(2, n + 1):
        #     for k in square:
        #         if k < i:
        #             dp[i] = min(dp[i], dp[i - k] + dp[k])
        # return dp[n]
        """
        官方题解1：贪心枚举。上述dp需要O(n^3/2)复杂度是因为需要遍历n之前所有数字并保存结果。但我们其实只需要用到
        n的结果，并且n的组合个数越小越好。如果可以使用一种方法从组合个数开始升序遍历，可以将复杂度降低在O(h/2)，h是
        可能发生的最大递归次数，因为虽然组合个数从1-n遍历，但不会遍历到n，会在某个点停下，事实上这个停下的个数不大。
        所以每次只需要递归判断可以用k个数组成n。
        """
        # def is_divide(n, cnt):
        #     if cnt == 1:
        #         return n in square
        #     for k in square:
        #         if is_divide(n - k, cnt - 1):
        #             return True
        #     return False
        #
        # square = set([i * i for i in range(1, int(n ** 0.5) + 1)])
        # for cnt in range(1, n + 1):
        #     if is_divide(n, cnt):
        #         return cnt
        """
        上述方法是从1开始遍历组合个数，通过递归实现判断是否可以成功组合。将递归调用栈考虑成树的话是一个N元树，即当前结点为
        (n,cnt)，所有的子节点为(n-k, cnt-1)，其中k是所有小于n的平方数。递归搜索的过程即为从上到下寻找叶节点中距离根节点
        最近的层数。可以使用BFS的方法模拟进行搜索，从根节点开始，保存减去所有小于该值的平方数之后作为下一次搜索的起点，直到找到
        当前值已经是平方数，返回对应层数。
        """
        # square = set([i * i for i in range(1, int(n ** 0.5) + 1)])
        # level = 0
        # queue = {n}
        # while queue:
        #     next_queue = set()
        #     level += 1
        #     for num in queue:
        #         if num in square:
        #             return level
        #         for sq in square:
        #             if sq < num:
        #                 next_queue.add(num - sq)
        #     queue = next_queue
        # return level
        """
        数学定理求解，具体见math/数学定理.docx
        """
        def is_square(n):
            sq = int((n ** 0.5))
            return sq * sq == n

        # 除以4^k
        while n & 3 == 0:
            n >>= 2
        # mod 8
        if n & 7 == 7:
            return 4
        if is_square(n):
            return 1
        for i in range(1, int(n ** 0.5) + 1):
            if is_square(n - i * i):
                return 2
        return 3


s = Solution()
print(s.numSquares(7691))
