#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/16 12:39
# @Author:JiahangGu
class Node:
    def __init__(self, c):
        self.c = c
        self.son = dict()
        self.end = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(0)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
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
        Returns if the word is in the trie.
        """
        head = self.root
        for i in range(len(word)):
            if word[i] not in head.son:
                return False
            else:
                head = head.son[word[i]]
        return head.end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        head = self.root
        for i in range(len(prefix)):
            if prefix[i] not in head.son:
                return False
            else:
                head = head.son[prefix[i]]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)