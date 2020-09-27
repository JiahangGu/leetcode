#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/15 15:09
# @Author:JiahangGu
from typing import List


class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        """
        分析题意，首先对s串的操作是选定子区间升序排序，也就意味着大的数字会到后面，如果target某个位置发现数字小的在数字大的后面，且
        后面都比较完成，则这个数组不能转换。
        可以从后往前遍历，对于不相等的s[i], t[i]，如果t[i] < s[i]则不可以转换，如果t[i]>s[i]则从s[i]向前查找到第一个t[i]的位置
        和邻点两两交换（如果逆序的话），如果非逆序则无法交换。如果可以遍历到0得到相同字符串，则可以交换得到
        :param s:
        :param t:
        :return:
        """
        # s_list = [c for c in s]
        # ptr_t, ptr_s = len(t)-1, len(s)-1
        # if ptr_s != ptr_t:
        #     return False
        # while ptr_t >= 0 and ptr_s >= 0:
        #     if s_list[ptr_s] == t[ptr_t]:
        #         pass
        #     elif s_list[ptr_s] > t[ptr_t]:
        #         return False
        #     else:
        #         idx = ptr_s - 1
        #         while idx >= 0 and s_list[idx] != t[ptr_t]:
        #             idx -= 1
        #         if idx < 0:
        #             return False
        #         for i in range(idx, ptr_s):
        #             if s_list[i] < s_list[i+1]:
        #                 return False
        #             s_list[i], s_list[i+1] = s_list[i+1], s_list[i]
        #     ptr_t -= 1
        #     ptr_s -= 1
        # return True
        """
        解法超时，通过样例129/131，但至少证明了思路是正确的。寻找一下可以优化的空间。首先就看到寻找s中出现的
        第一个t[i]，这里使用了两个循环一个查找另一个交换，但其实需要的信息是判断在找到的s对应字符的位置到t的位置
        之间是否有大于该数字的字符出现，因为一旦出现之后就无法交换。所以可以使用一个字典来记录每个数字出现的位置，
        如果该数字最右边的位置到t当前位置之间有大于的存在，则无法交换。而且，这里的邻点交换只是模拟，并不需要真的交换
        ，因为交换前后的子序列中的数字的相对位置不变。
        """
        from collections import defaultdict
        pos = defaultdict(list)
        p_t, p_s = len(t)-1, len(s)-1
        if p_t != p_s:
            return False
        for i, c in enumerate(s):
            pos[int(c)].append(i)
        while p_t >= 0:
            # 判断s中最右边的t[p_t]换到p_s的位置的途中是否存在大于t[p_t]的值
            if not pos[int(t[p_t])]:
                return False
            left_pos = pos[int(t[p_t])].pop(-1)
            for i in range(int(t[p_t])+1, 10):
                if pos[i] and pos[i][-1] > left_pos:
                    return False
            p_t -= 1
        return True


ss = Solution()
s = "12345"
t = "12435"
print(ss.isTransformable(s, t))
