#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/6 9:20
# @Author:JiahangGu
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        没有给定wordlist的长度范围，先尝试暴力法解决。
        使用回溯法，遍历单词列表找到满足题意的单词进行替换，并进入深层递归，如果不存在满足的单词则回溯。
        要求的是求所有转换路径中最小的，所以要遍历所有可行解并得到最小的解。
        运行结果超时，需要进行剪枝。剪枝策略有如下两个：
        1.单词的变换必须要朝着离endword至少不偏离的方向走，所以必须满足变换之后和endword的差距没有变小，可以使用一个字典存储
        单词到endword的距离，在递归过程中，每次首先向更近的点走，如果走不通退回来再走距离一样的路径，这样保证了第一个得到的结果
        是最优的，不需要找到一条路径之后再回溯。
        :param beginWord:
        :param endWord:
        :param wordList:
        :return:
        """
        # def get_diff(word1, word2):
        #     diff = 0
        #     for i in range(len(word1)):
        #         if word1[i] != word2[i]:
        #             diff += 1
        #     return diff
        #
        # def dfs(begin, end, num, cur_dis, length):
        #     nonlocal ans
        #     if begin == end:
        #         ans = num
        #         return True
        #     if cur_dis > length:
        #         return
        #     for i in range(cur_dis - 1, length + 1):
        #         for word in dis[i]:
        #             if flag[word] and get_diff(word, begin) == 1:
        #                 flag[word] = False
        #                 if dfs(word, end, num + 1, i, length):
        #                     return True
        #                 flag[word] = True
        #     return False
        #
        # from collections import defaultdict
        # dis = defaultdict(list)
        # flag = dict()
        # for word in wordList:
        #     flag[word] = True
        #     diff = get_diff(word, endWord)
        #     dis[diff].append(word)
        # if not flag.get(endWord, False):
        #     return 0
        # flag[beginWord] = False
        # ans = 0
        # length = len(endWord)
        # x = get_diff(beginWord, endWord)
        # dfs(beginWord, endWord, 1, x, length)
        # return ans
        """
        上述思路并不能第一次就找到最优解，因为可能在第二条路才最优。话说有用DFS找最小路径的吗，喂，当然是BFS啊。用BFS搜到的第一个解
        一定是最优解。所以思路清晰了起来，用一个队列维护当前待访问的单词，取出一个单词后，从单词列表中找出满足只有一位不同且未使用的单词，
        放入队列。只要出现目标单词就可以直接返回。
        存在的问题是，对于每个取出来的单词，都要遍历一次单词列表找满足条件的单词，效率很低。可以使用一个预处理方法来得到每个单词的替换方案。
        将单词的每个位置替换为*，则两个单词在替换后的结果是一样的，则说明可以通过替换一次得到。
        """
        # if endWord not in wordList:
        #     return 0
        # from collections import defaultdict
        # template_words = defaultdict(list)
        # l = len(endWord)
        # for word in wordList:
        #     for i in range(l):
        #         temp = word[:i] + "*" + word[i + 1:]
        #         template_words[temp].append(word)
        # q = [(beginWord, 1)]
        # visit = {beginWord: True}
        # while q:
        #     word, level = q.pop(0)
        #     for i in range(l):
        #         temp = word[:i] + "*" + word[i + 1:]
        #         for w in template_words[temp]:
        #             if w == endWord:
        #                 return level + 1
        #             else:
        #                 if w not in visit:
        #                     q.append((w, level + 1))
        #                     visit[w] = True
        # return 0
        """
        可以使用更多的空间换时间。这里要找的最短变换路径在BFS搜索到时只有一条，那么可以使用双向BFS，一端从begin开始，另一端从end开始，
        当二者在某一个单词处相遇时，说明这两个路径属于同一条，将二者合并即为最终结果。
        在上述解法的基础上，增加一个从end开始的visit和队列，当找到一个结点同时属于两个visit时（即两个都访问到），返回两个长度之和。
        """
        def bfs(word, level, q, visit, visit_other):
            for i in range(len(word)):
                temp = word[:i] + "*" + word[i + 1:]
                for w in template_words[temp]:
                    if w in visit_other:
                        return level + visit_other[w]
                    else:
                        if w not in visit:
                            visit[w] = level + 1
                            q.append((w, level + 1))
            return None

        if endWord not in wordList:
            return 0
        from collections import defaultdict
        template_words = defaultdict(list)
        l = len(endWord)
        for word in wordList:
            for i in range(l):
                temp = word[:i] + "*" + word[i + 1:]
                template_words[temp].append(word)
        q_begin = [(beginWord, 1)]
        q_end = [(endWord, 1)]
        visit_begin = {beginWord: 1}
        visit_end = {endWord: 1}
        ans = None
        while q_begin and q_end:
            begin, level_begin = q_begin.pop(0)
            ans = bfs(begin, level_begin, q_begin, visit_begin, visit_end)
            if ans:
                return ans
            end, level_end = q_end.pop(0)
            ans = bfs(end, level_end, q_end, visit_end, visit_begin)
            if ans:
                return ans
        return 0


s = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","log","cog"]
print(s.ladderLength(beginWord, endWord, wordList))
