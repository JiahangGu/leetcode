#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/3 16:22
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
        先用非in-place的方法做，首先得到整个树的前序遍历，然后做链接。递归方法太简单，这里用一下迭代方式复习下。
        :param root:
        :return:
        """
        # if not root:
        #     return
        # preorders = []
        # stack = []
        # node = root
        # while node or stack:
        #     while node:
        #         preorders.append(node)
        #         stack.append(node)
        #         node = node.left
        #     node = stack.pop()
        #     node = node.right
        # pre = preorders[0]
        # for i in range(1, len(preorders)):
        #     cur = preorders[i]
        #     pre.left = None
        #     pre.right = cur
        #     pre = cur
        """
        接下来是in-place修改，在迭代返回的时候做链表转换。用prev记录前一个节点，curr记录当前节点，如果prev非空，
        则prev.right=curr，此外还需要提前保存当前节点的左右子节点信息，并且由于要模拟递归，在用栈的时候需要先放
        右子节点然后放左子节点，这样在左子节点及其后代全部访问完成后才会进入右子节点对应的子树。
        """
        # if not root:
        #     return
        # stack = [root]
        # prev = None
        # while stack:
        #     curr = stack.pop()
        #     if prev:
        #         prev.left = None
        #         prev.right = curr
        #     if curr.right:
        #         stack.append(curr.right)
        #     if curr.left:
        #         stack.append(curr.left)
        #     prev = curr
        """
        第三种解法为不需要使用O(N)空间复杂度的做法，只需要O(1)保存每个节点的前驱节点，即每个点只要连接到该点的前驱节点即可。
        思路如下：当前节点的右子节点的前驱节点是当前节点的左子树的最右节点，当前节点的左子节点的前驱是该节点。可以看出，左子节点
        的前驱修改直接对该节点修改，而右子节点则要找到左子树的最右节点，在找到后，可以直接将该最右节点的right置为当前节点的
        右子节点，并且修改当前节点的right为当前节点的左子节点。这样修改下来，所有具有左子节点的节点都会被修改为right为左子节点，
        而左子节点的right为该节点的右子节点。相当于整棵树顺下来，将所有向左的分叉都修改为向下一条并入主干的链表。
        动画可能更清晰，见https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/solution/er-cha-shu-zhan-kai-wei-lian-biao-by-leetcode-solu/
        本题解同样参考自上述链接，想法还是很巧妙的。
        """
        if not root:
            return
        cur = root
        while cur:
            if cur.left:
                pre, nex = cur.left, cur.left
                while pre.right:
                    pre = pre.right
                pre.right = cur.right
                cur.left = None
                cur.right = nex
            cur = cur.right
