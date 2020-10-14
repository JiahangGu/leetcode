#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/8 10:40
# @Author:JiahangGu

class LinkNode:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, node):
        if not self.head:
            self.head = node
        elif not self.tail:
            self.tail = node
            self.head.next = node
            node.prev = self.head
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def remove(self, node):
        if node == self.head:
            self.head = node.next
            if self.head:
                self.head.prev = None
        elif node == self.tail:
            self.tail = node.prev
            if self.tail:
                self.tail.next = None
        else:
            tmp = node.prev
            tmp.next = node.next
            node.next.prev = tmp
        node.next = None
        node.prev = None

    def remove_head(self):
        node = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        return node

    def str(self):
        ans = []
        node = self.head
        while node:
            ans.append(node.val)
            node = node.next
        return ans

class LRUCache:

    def __init__(self, capacity: int):
        """
        使用哈希表实现O(1)查询，使用双向链表实现O(1)插入和删除
        查询的时候，首先判断是否存在，如果存在，则将该节点移动到tail的位置，表示是最新访问的
        写入数据时，首先判断容量是否足够，如果够直接放入到最后一位，如果不够，则移除掉head位置，并将新
        结点插入到tail位置。
        上述操作都要反应在哈希表中。
        :param capacity:
        """
        self.len = 0
        self.max_len = capacity
        self.d = dict()
        self.dll = DoubleLinkedList()

    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]
            self.dll.remove(node)
            self.dll.insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            node.val = value
            self.dll.remove(node)
            self.dll.insert(node)
            self.d[key] = node
        else:
            if self.len == self.max_len:
                node = self.dll.remove_head()
                k = node.key
                del self.d[k]
                self.len -= 1
            node = LinkNode(value, key)
            self.d[key] = node
            self.dll.insert(node)
            self.len += 1

    def str(self):
        return self.dll.str()


cache = LRUCache(2)
cache.put(1, 1)
print(cache.str())
cache.put(2, 2)
print(cache.str())
print(cache.get(1))
print(cache.str())
cache.put(3, 3)
print(cache.str())
print(cache.get(2))
print(cache.str())
cache.put(4, 4)
print(cache.str())
print(cache.get(1))
print(cache.str())
print(cache.get(3))
print(cache.str())
print(cache.get(4))
print(cache.str())
