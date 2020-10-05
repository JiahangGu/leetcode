#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/5 20:31
# @Author:JiahangGu

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        展开链表的顺序是前序遍历的顺序，可以在前序遍历算法中进行修改，记录一个前驱结点，则该节点的right为当前结点。
        此处使用迭代算法实现。
        首次尝试实现后发现会在赋值prev.right的时候破坏树原有的结构，导致死循环。
        这里有三种解决方案：
        1.将遍历和划分列表分开做，先得到前序遍历的列表，再对列表中的元素按顺序赋值right结点，空间复杂度为O(N)
        2.在遍历的同时做链表的展开。此前的方法问题出在会对树结构进行修改，导致后续回溯的时候得到的右子节点是修改过后的，解决的关键就
        在于在修改结构之前对右子节点进行存储，所以就需要在第一次访问到结点的时候，将该节点的左右子节点都放到栈中。注意要先放右子节点
        再放左子节点，同时使用prev记录前驱结点。实现完可以发现这个方式是在另一种迭代前序遍历的算法上进行修改，好处是在破坏树的结构之前
        已经保留了左右子节点的信息。
        """
        # if not root:
        #     return
        # stack = [root]
        # prev = None
        # while stack:
        #     node = stack.pop()
        #     if prev:
        #         prev.left = None
        #         prev.right = node
        #     prev = node
        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)
        """
        第三种方案：对于当前结点，找到其右子节点的前驱结点，即左子树中最右侧结点。解法原理是直接越过根节点将右子树拼接到左子树的最右子节点上，
        对于每一个存在左子树的根节点均进行这样的操作，在最终会得到一个展开的链表。注意这里拼接之后左子树就不存在了，遍历的时候只能移到右子树上。
        一个总结就是，首先熟练掌握不同的迭代遍历算法，可能在特定场景下某一个是有用的。比如这里是可以提前保留树结构信息，这是另一种方式达不到的。
        还有就是，思维的广度，这里的展开不一定要top-down，而是可以通过左右子树的关系完成超车。比如直到是前序遍历，那么将右子树直接接在左子树最
        右结点之后就提前完成了这一部分的前驱关系。而通过指针迁移，可以将二叉树改成单链表的形式。
        """
        cur = root
        while cur:
            if cur.left:
                prev = nex = cur.left
                while prev.right:
                    prev = prev.right
                prev.right = cur.right
                cur.right = nex
            cur = cur.right


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n1.left = n2
n1.right = n5
n2.left = n3
n2.right = n4
n5.right = n6
s = Solution()
print(s.flatten(n1))
