#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/8/28 17:36
# @Author:JiahangGu
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        """
        dfs从首数字向后搜索，如果当前数字大于当前递增序列的最后一位，则放入继续搜索，如果当前递增序列长度
        大于1则放入ans。
        如此解法存在重复解的问题，使用python自带的in可以解决重复问题，但不符合本道题的本意。重复问题应该抛开语言的特性，
        靠算法解决。解决重复解可以判断在当前递增序列中，从序列最后一位数字在原数组的位置开始
        到当前字符为止，该字符是否在原数组中出现过。例如[4,6,7,7]中，如果当前结果是[4,6]且遍历到3处，序列
        最后一个数字出现位置为1，而2的位置为7等于当前数字，则表示该数字已经计算过不需要加入，而如果当前结果为
        [4,6,7]，则从3开始查找发现没有相同的数字，则应该加入7
        :param nums:
        :return:
        """
        # def is_first(last, pos):
        #     """
        #     去重函数，判断当前pos位置的数字是否在之前的情况中统计过。原理是这样，如果在[last+1, pos)原数组中出现过
        #     nums[pos]，那么nums[pos]在此前一定统计过pos出现的情况，再次统计就会存在重复解。例如[4,6,7,4,4,4]在
        #     计算第2个4开头的序列时，由于last=-1，存在nums[0]=4，所以以4开头的序列一定都计算过，会跳过
        #     :param last:
        #     :param pos:
        #     :return:
        #     """
        #     for i in range(last+1, pos):
        #         if nums[i] == nums[pos]:
        #             return False
        #     return True
        #
        # def dfs(ans, last, pos, path):
        #     """
        #     递归放入符合条件的数字到当前递增序列中，且存在去重逻辑
        #     :param ans:
        #     :param last: 记录path最后一个数字在原数组中的位置
        #     :param pos: 记录当前遍历到的数组位置
        #     :param path:
        #     :return:
        #     """
        #     if pos >= len(nums):
        #         return
        #     # 注意下面的括号，and左侧是判断是否构成递增序列，而and右侧是判断是否存在重复解，所以需要加括号防止or短路
        #     # 如果这个元素合法那么选择加入这个元素
        #     if (not path or nums[pos] >= path[-1]) and is_first(last, pos):
        #         path.append(nums[pos])
        #         if len(path) > 1:
        #             ans.append(path[:])
        #         dfs(ans, pos, pos+1, path)
        #         path.pop()
        #     # 这个元素不合法，不加入
        #     dfs(ans, last, pos+1, path)
        # ans = []
        # path = []
        # dfs(ans, -1, 0, path)
        # return ans
        """
        进一步优化可以将判断去重的函数由O(n)降低到O(1)水平，可知函数的作用时判断last到pos之间是否包含nums[pos]，如果将
        nums[i]之前出现过的和nums[i]相等的元素位置记录下来，那么可以O(1)判断出是否重复。假设以pre[i]表示在i之前最后一次
        出现的nums[i]的位置，则is_first中可以根据last+1 < pre[pos] < pos来判断是否重复。
        """
        """
        此外还有官方题解的剪枝方法，原理很简单，如果当前数字大于等于递增序列的最大值就选择该元素，而如果该数字和前一个数字不相等
        才会不选择他进入下一层递归。首先，选择的情况很容易理解，大于等于前一个值的一定是没有遇到过的，也就是说不存在重复的情况，
        而不选择有两种情况，一个是和前一个相等，这个情况对应的序列在前一个数字的深层递归一定已经统计过，所以不需要跳过他进行后续
        的排列，会产生重复解；另一个不相等时表示后续的子数组还没有访问过，则进入深层递归。
        """
        """
        官方解法1，使用Rabin-Karp字符串编码方式，生成所有的字符串序列，然后判断是否满足条件。产生采用二进制编码选择数组对应
        元素的方式，即当前编码是0不选择，是1选择，共有2^n种情况。py实现超时
        解法2很简单有说明，不再实现，和上述第一种解法接近。同样是记录在当前递归层对应的最后一个递增序列是否会重复出现，以此排除
        重复情况。
        """
        def get_subsequences(mask):
            path.clear()
            for i in range(mask):
                if mask & 1:
                    path.append(nums[i])
                mask >>= 1

        def check():
            for i in range(1, len(path)):
                if path[i-1] > path[i]:
                    return False
            return len(path) >= 2

        def get_hash(base, mod):
            hash_value = 0
            for i in range(len(path)):
                hash_value = hash_value * base % mod + path[i]
                hash_value %= mod
            return hash_value

        ans = []
        path = []
        keys = set()
        n = len(nums)
        for i in range(1 << n):
            get_subsequences(i)
            hash_value = get_hash(261, 10**9+7)
            if check() and hash_value not in keys:
                ans.append(path[:])
                keys.add(hash_value)
        return ans


s = Solution()
print(s.findSubsequences([4, 6, 7, 4, 4, 4]))
