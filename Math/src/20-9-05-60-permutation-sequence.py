#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/5 14:41
# @Author:JiahangGu


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        由于n的最大值只有9，所以可以先回溯求出所有的排列，然后取出第k个返回。
        时间和空间复杂度均为O(n!)。
        :param n:
        :param k:
        :return:
        """
        # def permutation(cur, n):
        #     if cur == n-1:
        #         ans.append(nums[:])
        #         return
        #     for i in range(cur, n):
        #         nums[i], nums[cur] = nums[cur], nums[i]
        #         permutation(cur+1, n)
        #         nums[i], nums[cur] = nums[cur], nums[i]
        #
        # nums = [i for i in range(1, n+1)]
        # ans = []
        # permutation(0, n)
        # ans.sort()
        # res = [str(x) for x in ans[k-1]]
        # return "".join(res)
        """
        发现全排列之后顺序不对，因为[1,2,3]在交换之后会先得到[3,2,1]然后才有[3,1,2]。此外求全排列导致复杂度高，O(n!)，
        其实已知序列是1-n这个条件并没有用到。
        因为每一个长度为n的序列排列数为n!，那么可以根据k的值依次确定首位元素的值。给定n，k，如果
        x*(n-1)!<=k<=(x+1)*(n-1)!，则x位应该是当前的第一位，将nums[x]换到第一位之后，剩余的数组排序后继续进行上述操作
        注意要求的第k个，在求排列顺序的时候是从0开始的，所以第一层递归时需要用k-1.
        """
        # def fact(n):
        #     ans = 1
        #     for i in range(1, n+1):
        #         ans *= i
        #     return ans
        #
        # def dfs(nums, k, n):
        #     nums.sort()
        #     if k == 0:
        #         ans.extend(nums)
        #         return
        #     fact_n = fact(n-1)
        #     x = k // fact_n
        #     nums[0], nums[x] = nums[x], nums[0]
        #     ans.append(nums[0])
        #     dfs(nums[1:], k - x * fact_n, n-1)
        #
        # nums = [i for i in range(1, n+1)]
        # ans = []
        # dfs(nums, k-1, n)
        # return "".join([str(x) for x in ans])
        """
        参考官方题解的迭代算法，思路同上，主要是一个记录数字的小技巧，使用长度为n的只有1的数组，标记每个元素是否使用，求出
        当前的首元素位置（此时的元素位置表示的是剩余数字中从小到大排序之后的位置，比如剩下[2，1,4]，而求出位置为2，则应该
        选择2为下一个元素。求出位置后逐个减去1的数组，得到0时就是所在位置，不需要排序。
        """
        fact = [1] * (n + 1)
        for i in range(2, n + 1):
            fact[i] = i * fact[i - 1]
        ans = []
        flag = [1] * (n + 1)
        k -= 1
        for i in range(1, n + 1):
            pos = k // fact[n - i] + 1
            for j in range(1, n + 1):
                pos -= flag[j]
                if pos == 0:
                    ans.append(str(j))
                    flag[j] = 0
                    break
            k %= fact[n - i]
        return "".join(ans)


s = Solution()
print(s.getPermutation(3, 5))
