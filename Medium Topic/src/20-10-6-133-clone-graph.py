#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/6 15:58
# @Author:JiahangGu
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        深拷贝的关键是，对于图中每个节点都要新建一个同样值的新节点，并建立节点之间的联系。
        遍历需要一个标记数组记录所有访问过的节点（这里访问过的节点是指已经生成邻居节点的点），并且在第一次生成的时候
        避免增加双向环，即a的邻居b只是新建b加到新建a的邻居，新建b的邻居不需要加上新建a，否则会导致重复生成，因为新建b
        也是需要再次访问的，而在访问过程中是遍历原始点邻居并将对应新建结点加入到新节点的邻居中。
        :param node:
        :return:
        """
        # def dfs(cur_node):
        #     visit.add(cur_node)
        #     for n in cur_node.neighbors:
        #         if n not in flag:
        #             new_n = Node(n.val)
        #         else:
        #             new_n = flag[n]
        #         flag[n] = new_n
        #         flag[cur_node].neighbors.append(new_n)
        #         if n not in visit:
        #             dfs(n)
        #
        # flag = dict()
        # visit = set()
        # root = Node(node.val)
        # flag[node] = root
        # dfs(node)
        # return root
        """
        另一种解法DFS也是同理，只是更巧妙，在这里记录一下。在生成结点的过程中，如果邻居没有新建结点，则新建并进入该节点的递归层，
        当递归完成后再将该节点加入到当前结点的邻居点中。这样可以保证新建的点只会加入到邻居中一次，并且该节点的邻居已经重建完成。
        如果遍历过程发现该节点已经建立，则必定是一个完整的结点（包括所有邻居点），因为建点之后立即进行递归建立邻居点。
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