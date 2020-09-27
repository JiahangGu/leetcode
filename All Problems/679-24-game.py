#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/8/28 22:42
# @Author:JiahangGu
from typing import List


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        """
        起初被这道题的建模搞得有点困惑，因为数字加减乘除可以模拟，但括号如何反映在计算公式或者函数中呢？
        考虑到括号在计算公式中的作用是提高某一个计算的优先级，例如相邻的加减通过括号提升到大于乘除的优先级，
        那在递归中可以通过递归层数来表示计算的优先级，例如根据递归参数的不同可以获得不同的计算优先级，四个参数
        的递归函数为第一级，三个参数的为第二级，并且4到3的参数变化则是决定优先级的计算，可以形成多种组合（abcd之间
        两个数字的多种操作），进入到下一级递归时就表示当前计算是以此前递归调用层的参数部分为优先计算的，从而确定了
        整个公式的计算优先级，并在调用深层递归时组合不同的计算表达符号得到所有的计算组合。
        总之，通过递归层数解决了括号问题，这个问题难度就很小了。
        注意在这里需要用到除法要保证除数不能为0，并且这里是浮点操作，不能直接判断==，而是通过与一个较小的值比较判断是否相等。
        :param nums:
        :return:
        """
        # def dfs_3(a, b, c):
        #     flag = dfs_2(a+b, c) or dfs_2(a-b, c) or dfs_2(b-a, c) or dfs_2(a*b, c) \
        #         or dfs_2(b+c, a) or dfs_2(b-c, a) or dfs_2(c-b, a) or dfs_2(b*c, a) \
        #         or dfs_2(a+c, b) or dfs_2(a-c, b) or dfs_2(c-a, b) or dfs_2(a*c, b)
        #     if not flag and a != 0:
        #         flag = dfs_2(b/a, c) or dfs_2(c/a, b)
        #     if not flag and b != 0:
        #         flag = dfs_2(a/b, c) or dfs_2(c/b, a)
        #     if not flag and c != 0:
        #         flag = dfs_2(a/c, b) or dfs_2(b/c, a)
        #     return flag
        #
        # def dfs_2(a, b):
        #     flag = abs(a+b-24)<1e-5 or abs(a-b-24)<1e-5 or abs(b-a-24)<1e-5 or abs(a*b-24)<1e-5
        #     if not flag and a != 0:
        #         flag = flag or abs(b/a-24)<1e-5
        #     if not flag and b != 0:
        #         flag = flag or abs(a/b-24)<1e-5
        #     return flag
        #
        # nums.sort()
        # a, b, c, d = tuple(nums)
        # flag = dfs_3(a+b, c, d) or dfs_3(a-b, c, d) or dfs_3(b-a, c, d) or dfs_3(a*b, c, d) \
        #     or dfs_3(b+c, a, d) or dfs_3(b-c, a, d) or dfs_3(c-b, a, d) or dfs_3(c*b, a, d) \
        #     or dfs_3(c+d, a, b) or dfs_3(c-d, a, b) or dfs_3(d-c, a, b) or dfs_3(c*d, a, b) \
        #     or dfs_3(a+c, b, d) or dfs_3(a-c, b, d) or dfs_3(c-a, b, d) or dfs_3(a*c, b, d) \
        #     or dfs_3(a+d, b, c) or dfs_3(a-d, b, c) or dfs_3(d-a, b, c) or dfs_3(a*d, b, c) \
        #     or dfs_3(b+d, a, c) or dfs_3(b-d, a, c) or dfs_3(d-b, a, c) or dfs_3(b*d, a, c)
        # if not flag and a != 0:
        #     flag = flag or dfs_3(b/a, c, d) or dfs_3(c/a, b, d) or dfs_3(d/a, b, c)
        # if not flag and b != 0:
        #     flag = flag or dfs_3(a/b, c, d) or dfs_3(c/b, a, d) or dfs_3(d/b, a, c)
        # if not flag and c != 0:
        #     flag = flag or dfs_3(a/c, b, d) or dfs_3(b/c, a, d) or dfs_3(d/c, a, b)
        # if not flag and d != 0:
        #     flag = flag or dfs_3(a/d, b, c) or dfs_3(b/d, a, c) or dfs_3(c/d, a, b)
        # return flag
        """
        上述解法存在一些冗余，每次都需要从给定的数字中选出两个作为组合，一是程序显得冗长，而是当数字变多时这种解法不再适用。
        上面的递归无非是在解决一个问题：括号决定了计算公式的操作符优先级。所以括号的作用就可以理解为在三个操作符和四个数字中
        选择两个数字和一个操作符得到结果，并且将这个结果放回到候选数组中，这样结果就剩下3数字和2个操作符，依然可以使用这样的
        思想递归减少直到数组中只剩一个数字，而这个数字就是当前括号和操作符选择得到的最终计算结果，判断是不是24即可。
        """
        def dfs(arr):
            if len(arr) == 1 and abs(arr[0]-24) < 1e-5:
                return True
            if len(arr) <= 1:
                return False
            for i, x in enumerate(arr):
                for j, y in enumerate(arr):
                    if i != j:
                        # 将操作符涉及不到的数字加入到新的数组中，以待下次递归使用
                        new_arr = []
                        for k, z in enumerate(arr):
                            if k != i and k != j:
                                new_arr.append(z)
                        for k in range(4):
                            # 如果当前操作是加法或乘法，并且i>j表示已经得到结果，因为满足交换律，并且i<j的结果已经计算完成
                            if k < 2 and i > j:
                                continue
                            elif k == 0:
                                new_arr.append(x+y)
                            elif k == 1:
                                new_arr.append(x*y)
                            elif k == 2:
                                new_arr.append(x-y)
                            elif k == 3:
                                # 等于0时要跳过，不然会进入到后面的if和pop，导致出错
                                if abs(y) < 1e-5:
                                    continue
                                new_arr.append(x/y)
                            if dfs(new_arr):
                                return True
                            new_arr.pop()
            return False
        return dfs(nums)


s = Solution()
nums = [1,2,1,2]
print(s.judgePoint24(nums))
