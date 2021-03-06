#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/11/2 20:13
# @Author:JiahangGu
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        最简单的做法：双重循环做查找，时间复杂度为O(N2)。
        稍微进阶一点：使用环形查找，即对于每个数字放到应该在的位置，如2应放在第二个位置，直到所有数字归位或者
        途中出现归位时已有的数字，则表示重复，但是需要修改数组，不符合题意。
        空间换时间的做法：记录每个数字出现次数即可。空间O(N)。
        位运算：如果只有一个数字出现两次，则可以用异或算[1,n]结果并与数组异或，剩下的就是重复的数，但是本题
        可能出现多于两次，这里不适用。
        鉴于题目中的多个要求，可以在环形查找的方法上进阶修改。首先要求的是不修改原数组，则需要在环形遍历的时候
        记录下环的位置（入口），因为上述做法一遍修改一遍搜索，遇到第一个环就可以确定出是哪个重复数字，同理，只要
        在遍历的时候记录下环的入口，就可以在环中找到重复数字。寻找环的方法使用快慢指针即可。
        这里涉及到的一个推导：为什么在slow和fast相遇后，从0和slow出发移动到相遇的点就是答案。假设环长为L，从起点到
        环的入口步数为a，从环的入口继续走b步到达相遇位置，从相遇位置继续走c步回到环的入口，则有b+c=L。并且可知，
        慢指针走了a+b步，快指针走了2(a+b)步，在相遇位置，快指针比慢指针夺走了若干圈，即2(a+b)=a+b+kL，得到a=kL-b=(k-1)L+c，
        可知，如果从起点出发慢指针走a步到达环的入口，而此时快指针已经走了k-1圈之后又走了c步，由于从相遇位置走c步即可回到环的入口，因此
        也到达入口，两个指针在入口相遇
        :param nums:
        :return:
        """
        # slow, fast = nums[0], nums[nums[0]]
        # while slow != fast:
        #     slow, fast = nums[slow], nums[nums[fast]]
        # p1, p2 = 0, slow
        # while p1 != p2:
        #     p1, p2 = nums[p1], nums[p2]
        # return p1
        """
        解法2：给定了数字范围是[1,n]，所以可知如果小于i的数字均没有重复出现时，小于i的数字个数刚好为i，假设为cnt，如果某一个数字cnt>i则说明
        小于等于i的数字中出现了重复数字，如果cnt<=i则说明重复数字一定大于i，可以使用一个二分搜索查找出，每次查找需要统计下当前mid对应的cnt，
        所以总的复杂度为O(nlgn)，满足题意。
        注意二分的时候范围是[0,n-1]，但给定数组范围为[1,n]，需要对mid+1转换下。
        """
        # l, r = 0, len(nums) - 1
        # while l < r:
        #     mid = l + (r - l) // 2
        #     cnt = 0
        #     for i in range(len(nums)):
        #         if nums[i] <= mid + 1:
        #             cnt += 1
        #     if cnt <= mid + 1:
        #         l = mid + 1
        #     else:
        #         r = mid
        # return l + 1
        """
        解法3：二进制解法。如果将数组所有数字用二进制表示，则[1-n]中不包含重复数字的时候得到每个位上1的个数是固定的，
        如果包含重复数字，则重复数字的二进制表示中所有1对应的位上的个数都会大于不包含重复数字情况下的个数，即如果出现
        二进制1的个数大于[1-n]中对应的位则说明该位是由于重复数字出现导致的，所以重复数字在该位是1，最后将所有1表示出
        来即可。
        """
        n = len(nums) - 1
        tmp = n
        bit_num = 0
        while tmp:
            bit_num += 1
            tmp >>= 1
        ans = 0
        for i in range(bit_num):
            # 记录当前位上数组和[1,n]上1的个数，如果x > y则表示重复数字在该位为1
            x, y = 0, 0
            for j in range(n + 1):
                x += (nums[j] & (1 << i))
                if j > 0:
                    y += (j & (1 << i))
            if x > y:
                ans += 1 << i
        return ans


s = Solution()
print(s.findDuplicate([1,3,4,2,2]))
