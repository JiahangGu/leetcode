#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/26 21:20
# @Author:JiahangGu
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        结点的next指针其实就是指向层次遍历结果中该节点的下一个指针，此前使用的层次遍历的方法是BFS，会使用一个栈
        存储一层的结点，最大的栈长度可能为n/2，空间复杂度为O(n)。如果可以使用DFS求得层次遍历结果，就可以在其中只通过
        一个全局变量记录之前访问的结点，从而实现常量级空间复杂度。
        首先实现一下BFS层次遍历的算法，也算熟悉一下。
        :param root:
        :return:
        """
        # if not root:
        #     return root
        # q = [root]
        # while q:
        #     size = len(q)
        #     for i in range(size):
        #         node = q.pop(0)
        #         if i < size - 1:
        #             node.next = q[0]
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        # return root
        """
        BFS方法时间击败41%，内存击败78%。
        下面尝试DFS+O(1)空间复杂度的解法。
        首先如果一个节点是左子节点且父节点存在右子节点，那么next为右子节点。否则就要找到父节点的祖先节点的
        右子树对应的相同level的最左子节点。
        应该注意到（也是解题的关键，我怎么就没想到），在建立了next之后，可以通过next指针实现该层的层次遍历，
        也就是说，此前困扰很久的问题，寻找上述第二种情况的next节点，可以通过上一层已经建立好的next指针，去寻找符合
        next条件的结点。
        具体做法是，在第n层建立第n+1层的next链接，因为第n层已经有next链接，所以对子节点增加next时，可以方便得到
        该层的下一个next结点，并且找到第n+1层的下一个结点。
        使用leftmost记录第n+1层的最左结点，pre记录当前第n+1层结点的前驱结点，只有pre==none时记录leftmost为当前结点
        """
        # def get_next(child, pre, leftmost):
        #     if child:
        #         if pre:
        #             pre.next = child
        #         else:
        #             leftmost = child
        #         pre = child
        #     return pre, leftmost
        #
        # leftmost = root
        # pre = None
        # while leftmost:
        #     cur = leftmost
        #     leftmost = None
        #     while cur:
        #         pre, leftmost = get_next(cur.left, pre, leftmost)
        #         pre, leftmost = get_next(cur.right, pre, leftmost)
        #         cur = cur.next
        # return root
        """
        参考其余题解发现有其余有趣的解法，在这里一并记录，思路都是和上述一样，利用next会构建出同层的链表。
        构建一个dumm虚拟结点作为同层链表的首节点，next为真正的树的首节点。
        """
        cur = root
        while cur:
            dumm = Node()
            pre = dumm
            while cur:
                if cur.left:
                    pre.next = cur.left
                    pre = pre.next
                if cur.right:
                    pre.next = cur.right
                    pre = pre.next
                cur = cur.next
            cur = dumm.next
        return root

