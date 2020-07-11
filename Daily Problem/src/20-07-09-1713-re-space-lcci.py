#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/7/11 11:10
# @Author:JiahangGu
from typing import List


class Trie:
    def __init__(self):
        self.root = {}
        self.word_end = "_end"

    def insert(self, word):
        cur_node = self.root
        for char in word[::-1]:
            if char not in cur_node:
                cur_node[char] = {}
            cur_node = cur_node[char]
        cur_node[self.word_end] = True


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        '''
        要求未识别的字符数，每个位置的字符都有可能加上之前的字符串然后出现在字典中，所以需要
        从之前的字符开始，验证加上该字符后的单词是否出现在字典中，如果出现，则更新该字符位置
        的最小未识别字符数为使用该单词的最小值。
        定义dp[i]表示到位置i时的最小未识别字符数
        初始状态下dp[0]=0
        最终解为dp[n-1]
        定义状态转移方程：dp[i]=min(dp[i], dp[i-k]) if sentence[i-k...i] in dict for k in range(0, i-1)
        如果加上这个字符没能形成在字典出现的字符则dp[i]=dp[i-1]+1
        :param dictionary:
        :param sentence:
        :return:
        '''
        # dp = [0] * len(sentence) + [0]
        # dic = {word: True for word in dictionary}
        # for i in range(1, len(sentence)+1):
        #     dp[i] = dp[i-1] + 1
        #     for k in range(0, i):
        #         word = sentence[k:i]
        #         if word in dic:
        #             dp[i] = min(dp[i], dp[k])
        # return dp[-1]
        '''
        Trie字典树优化。上述存在的问题是，用哈希表实现本身常熟很大，然后在判断子串是否出现在字典中时，
        没必要全部枚举，只要前缀不存在那单词一定也不存在。比如xassad判断出xa不在字典中时已经没有必要
        继续搜索，因为肯定不存在。Trie字典树可参考Hash下介绍
        这里说明下字典树为什么要逆序存储字典的单词：因为想在查找时一次循环找到所有可能单词，如果正序就
        需要从此前的每个位置均出发一次查找该位置到当前字符位置对应的单词是否存在，会存在很多重复的子空
        间，而倒序的话，可以从当前位置出发向前搜索所有可能的单词，只需要一次遍历。
        '''
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        dp = [0] * len(sentence) + [0]
        for i in range(1, len(sentence)+1):
            dp[i] = dp[i-1] + 1
            cur_node = trie.root
            for k in range(i, 0, -1):
                char = sentence[k-1]
                if char not in cur_node:
                    break
                elif trie.word_end in cur_node[char]:
                    dp[i] = min(dp[i], dp[k-1])
                cur_node = cur_node[char]
        return dp[-1]


s = Solution()
dictionary = ["looked","just","like","her","brother"]
sentence = "jesslookedjustliketimherbrother"
print(s.respace(dictionary, sentence))
