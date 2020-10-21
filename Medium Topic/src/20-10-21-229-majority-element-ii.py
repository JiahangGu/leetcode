#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/21 9:43
# @Author:JiahangGu
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        首先超过是严格大于，所以超过n/3次的最多有两个元素，即结果为1或2个。
        回想求一个众数的做法：摩尔投票法，记录当前出现数字的次数，如果遍历到的数字等于当前数字，则次数加1，
        否则减1，如果减到0则说明不是最多次数的，更新为当前数字。
        求两个众数则记录两个数字和次数，都不出现时就都减1，有一个出现时对应次数+1，如果某个出现次数为0，则更新为当前数字。
        注意更新的顺序是应该先判断更新后修改，否则可能出现更新之后后面的值依然是更新之前的数字，丢失情况。
        注意摩尔投票法得到的最后数字可能不是最多次数，所以需要判断出现次数。
        :param nums:
        :return:
        """
        n = len(nums)
        num1 = nums[0]
        num2 = nums[0]
        cnt1, cnt2 = 0, 0
        for i in range(n):
            if nums[i] == num1:
                cnt1 += 1
                continue
            if nums[i] == num2:
                cnt2 += 1
                continue
            else:
                if cnt1 == 0:
                    num1 = nums[i]
                    cnt1 = 1
                elif cnt2 == 0:
                    num2 = nums[i]
                    cnt2 = 1
                else:
                    cnt1 -= 1
                    cnt2 -= 1
        cnt1 = 0
        cnt2 = 0
        for i in range(n):
            if nums[i] == num1:
                cnt1 += 1
            elif nums[i] == num2:
                cnt2 += 1
        ans = []
        if cnt1 > n // 3:
            ans.append(num1)
        if cnt2 > n // 3:
            ans.append(num2)
        return ans


s = Solution()
print(s.majorityElement([3,3,1,1,1,1,2,4,4,3,3,3,4,4]))
