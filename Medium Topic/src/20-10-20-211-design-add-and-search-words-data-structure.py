#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/20 11:51
# @Author:JiahangGu
class Node:
    def __init__(self, c):
        self.c = c
        self.son = dict()
        self.end = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        在字典树的基础上实现一个回溯算法，即如果碰到搜索的字符含有.，则.对应的位置应该搜索该节点的所有子节点。
        """
        self.root = Node(0)

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        head = self.root
        for i in range(len(word)):
            if word[i] in head.son:
                head = head.son[word[i]]
            else:
                node = Node(word[i])
                head.son[word[i]] = node
                head = node
        head.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def dfs(head, target):
            if len(target) == 0:
                return head.end
            if target[0] == '.':
                for k, v in head.son.items():
                    if dfs(v, target[1:]):
                        return True
            elif target[0] in head.son:
                return dfs(head.son[target[0]], target[1:])
            return False

        head = self.root
        return dfs(head, word)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)