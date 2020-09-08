#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/4 15:50
# @Author:JiahangGu

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        图的深拷贝就是遍历一次图，将图的节点和边复制下来，只是所有的节点和边都是新生成的对象。
        遍历可以使用DFS或BFS，这里提供两种解法。
        :param node:
        :return:
        """
        """
        DFS算法：同理BFS，从初始节点开始，并构造visit字典存储源节点对应的节点。如果邻居节点没有访问过，则构造新的
        克隆节点并加入到visit中。
        """
        def dfs(n):
            for neighbor in n.neighbors:
                if neighbor not in visit:
                    visit[neighbor] = Node(neighbor.val, [])
                    dfs(neighbor)
                visit[n].neighbors.append(visit[neighbor])

        if not node:
            return None
        visit = dict()
        visit[node] = Node(node.val, [])
        dfs(node)
        return visit[node]
        """
        BFS算法，将初始节点放入队列中，并构造visit字典存储原节点对应的新节点，在每次取出当前节点后，
        遍历邻居，如果该邻居节点没有访问过，则表明该节点同时没有克隆，所以先克隆一个节点并加入到当前节点
        的邻居集合中，并将该节点加入到队列中留待下次访问
        """
        # if not node:
        #     return None
        # root = Node(node.val, [])
        # q = [node]
        # visit = dict()
        # visit[node] = root
        # while q:
        #     n = q.pop(0)
        #     for neighbor in n.neighbors:
        #         if neighbor not in visit:
        #             q.append(neighbor)
        #             visit[neighbor] = Node(neighbor.val, [])
        #         visit[n].neighbors.append(visit[neighbor])
        # return visit[node]
