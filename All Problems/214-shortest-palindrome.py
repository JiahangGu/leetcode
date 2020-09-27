#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/2 21:47
# @Author:JiahangGu


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
        初始想法：由于只能在字符串前面加字符，则加完之后的回文子串的中心应该在原始字符串的前半部分，因为以后半部分为中心的回文串
        无法通过在字符串前面加字符得到，也就是说，前半部分加字符决定了后半部分的模式串的逆序会包含前半部分的子序列。例如aacecaaa中
        caaa的逆序aaac包含aac，所以在前面加一个a；abcd由于不存在如此的包含关系，所以要增加三个字符。
        这样就可以得到如下方案：遍历前半部分得到最大的回文子串长度对应的中心为最终串的中心，然后遍历右侧字符串对应补全即可，注意这里的
        前半部分的最大回文子串必须从第一个字符开始，也就是该字符串的前缀中的最大回文子串。
        :param s:
        :return:
        """
        # def get_length(pos):
        #     # 求奇数回文长度
        #     length_odd = 1
        #     l = pos - 1
        #     r = pos + 1
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         length_odd += 2
        #         l -= 1
        #         r += 1
        #     if l != -1:
        #         length_odd = 1
        #     # 求偶数回文长度
        #     length_even = 0
        #     l = pos
        #     r = pos + 1
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         length_even += 2
        #         l -= 1
        #         r += 1
        #     if l != -1:
        #         length_even = 0
        #     if length_odd >= length_even:
        #         return length_odd, True
        #     else:
        #         return length_even, False
        #
        # if not s:
        #     return ""
        # idx = 0
        # max_length = 0
        # n = len(s)
        # flag = True
        # final_flag = True
        # for i in range(n):
        #     length, flag = get_length(i)
        #     if length > max_length:
        #         idx = i
        #         max_length = length
        #         final_flag = flag
        # ans = []
        # if final_flag:
        #     ans = [s[idx]]
        #     idx += 1
        #     while idx < len(s):
        #         ans.append(s[idx])
        #         ans.insert(0, s[idx])
        #         idx += 1
        #
        # else:
        #     idx += 1
        #     while idx < len(s):
        #         ans.append(s[idx])
        #         ans.insert(0, s[idx])
        #         idx += 1
        # return "".join(ans)
        """
        上述方法超时，因为在每个位置的判断平均需要n/2即O(n)的复杂度，而共有n个位置，总复杂度为O(n2)。最后两个样例无法通过。
        这就需要在其上进行优化。本题解答分为两部分：1是遍历每一个回文子串的结束点，这里是无法优化的，因为任何一个位置都有可能
        成为回文子串的结束位置；2是判断子串的前缀是否是回文子串，当前实现复杂度为O(n)，但可以利用前缀信息优化到O(1)，这样就
        降低了一个量级的复杂度。
        O(n)求解最长回文的方法有两个：
        1.Rabin-Karp算法，即字符串编码算法，将字符串看作一个base进制的数，对应的十进制就是得到的hash数，在对模数取模之后，
        如果得到相同的hash数则说明两个字符串相等，因为hash冲突在这里的概率非常低可以忽略。
        2.KMP算法，见下一块注释。
        """
        # n = len(s)
        # last = -1
        # base, MOD = 131, 10 ** 9 + 7
        # mul = 1
        # # left和right分别表示当前字符结尾的字符串正序和逆序对应的hash值，如果两个相等则表示当前字符串是回文子串，因为一个字符串正序逆序相等是回文
        # left, right = 0, 0
        # for i in range(n):
        #     left = (left * base + ord(s[i])) % MOD
        #     right = (right + ord(s[i]) * mul) % MOD
        #     if left == right:
        #         last = i
        #     mul = mul * base % MOD
        # return s[::-1] + s[last+1:]
        """
        KMP算法实现O(n)复杂度求解最长回文。首先假设s1是s的前缀，s'是s反转后的字符串，且s1'是s'的后缀，如果s是一个回文字串，那么
        应该满足s1也出现在s'中且是s'的后缀，即s1=s1'。以s'为目标串，s为模式串进行匹配，如果能够完全匹配，则说明整个都是回文字串，如果不能
        那么在模式串匹配到的索引i处就是回文子串结束的位置。
        注意KMP算法实现过程中i,j的使用，很容易出现相反的错误，尽量使用更清晰的命名方式。
        """
        n = len(s)
        fail = [-1] * n
        # pattern_ptr = 0
        # prefix_ptr = -1
        # # 求next数组，因为next是关键字，这里使用fail表示，就意义来说是匹配失败需要回溯的
        # while pattern_ptr < n - 1:
        #     if prefix_ptr == -1 or s[pattern_ptr] == s[prefix_ptr]:
        #         # 当前相等要后移
        #         pattern_ptr += 1
        #         prefix_ptr += 1
        #         # 如果不同，则[0,prefix_ptr-1]的字串是相等的，可以回退到prefix_ptr的位置，从而跃进最大步
        #         if s[pattern_ptr] != s[prefix_ptr]:
        #             fail[pattern_ptr] = prefix_ptr
        #         # 如果当前模式串指向字符等于前缀指针指向的字符，那回退到prefix_ptr的位置也不可能匹配，所以要回退到更早的位置
        #         else:
        #             fail[pattern_ptr] = fail[prefix_ptr]
        #     else:
        #         # 不相等的情况下表明后续更不可能出现匹配，将前缀指针前移
        #         prefix_ptr = fail[prefix_ptr]
        for i in range(1, n):
            j = fail[i - 1]
            while j != -1 and s[j + 1] != s[i]:
                j = fail[j]
            if s[j + 1] == s[i]:
                fail[i] = j + 1
        pattern_ptr, target_ptr = 0, 0
        s_reverse = s[::-1]
        while target_ptr < n and pattern_ptr < n:
            if pattern_ptr == -1 or s[pattern_ptr] == s_reverse[target_ptr]:
                target_ptr += 1
                pattern_ptr += 1
            else:
                pattern_ptr = fail[pattern_ptr]
        if pattern_ptr == n:
            return s
        else:
            return s_reverse[:n-pattern_ptr] + s


s = Solution()
print(s.shortestPalindrome("abbacd"))
