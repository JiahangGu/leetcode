#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/3 16:24
# @Author:JiahangGu

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        空间复杂度为O(n)的解法很简单，只需要中序遍历一次树，得到的序列和应该得到的升序序列做对比，
        交换元素分为两种情况：1是交换两个不相邻的数字，则得到一个序列满足存在两个i<j and nums[i]>nums[j]，这时
        交换最左边的i和最右边的j对应的数字；2是交换相邻的数字，此时只有一个i<j and nums[i]>nums[j]，交换二者即可
        可以先中序得到序列，找到对应数字后去二叉树中找到数字交换，默认二叉树中不存在重复数字。
        空间复杂度为O(n)。
        :param root:
        :return:
        """
        # def dfs(r):
        #     if not r:
        #         return
        #     dfs(r.left)
        #     nums.append(r.val)
        #     dfs(r.right)
        #
        # def solve(r):
        #     nonlocal swap1, swap2
        #     if not r:
        #         return
        #     solve(r.left)
        #     if r.val == swap1:
        #         r.val = swap2
        #     elif r.val == swap2:
        #         r.val = swap1
        #         return
        #     solve(r.right)
        #
        # nums = []
        # dfs(root)
        # inverse = []
        # # 得到交换项，一个或者两个
        # for i in range(len(nums)-1):
        #     if nums[i] > nums[i+1]:
        #         inverse.append((nums[i], nums[i+1]))
        # if len(inverse) == 2:
        #     swap1, swap2 = inverse[0][0], inverse[1][1]
        # elif len(inverse) == 1:
        #     swap1, swap2 = inverse[0][0], inverse[0][1]
        # solve(root)
        """
        上述方法是使用一个O(n)的数组保存中序遍历的结果，但其实可以看出，只需要保存的结果是一个或两个逆序的数字对，在遍历完成之后交换这两个
        节点的值即可。可以记录两个需要交换的节点，swap1和swap2，如果出现逆序的对赋值swap1和swap2，如果出现两次则保留swap1，修改swap2，
        可以使用递归实现，在left之后的程序中加入。
        空间复杂度为O(m)，m表示树的最大深度，还没有达到O(1)的要求，但速度已经很快了。
        """
        # def dfs(r):
        #     nonlocal pre, swap1, swap2
        #     if r.left:
        #         dfs(r.left)
        #     if pre and pre.val > r.val:
        #         if not swap1 and not swap2:
        #             swap1, swap2 = pre, r
        #         else:
        #             swap2 = r
        #     pre = r
        #     if r.right:
        #         dfs(r.right)
        #
        # if not root:
        #     return
        # pre = None
        # swap1, swap2 = None, None
        # dfs(root)
        # swap1.val, swap2.val = swap2.val, swap1.val
        """
        这里尝试一下迭代法解题，也是对迭代法进行中序遍历再熟悉一遍。同上述解法，还是记录每个节点的pre节点，并比较大小进行记录。
        注意这里，此前的迭代解法是会对树进行修改的，例如会有cur.left=None，而本题要求不可以修改树其余节点，所以采用另一种迭代解法。
        """
        # if not root:
        #     return
        # pre = None
        # swap1, swap2 = None, None
        # stack = []
        # cur = root
        # while stack or cur:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left
        #     # 这里记录当前节点的前缀点并比较是否需要替换
        #     cur = stack.pop()
        #     if pre and pre.val > cur.val:
        #         if not swap1 and not swap2:
        #             swap1, swap2 = pre, cur
        #         else:
        #             swap2 = cur
        #     pre = cur
        #     cur = cur.right
        # swap1.val, swap2.val = swap2.val, swap1.val
        """
        哟西，时间击败了99%的人，但依然没有达到题目要求的空间复杂度O(1)，因为模拟递归的过程用栈保存了最大深度的所有节点。
        空间复杂度为O(1)的中序遍历算法只有Morris中序遍历算法，在Tree/下文档记录
        注意这里的前驱节点prev作用仍旧和Morris算法中的一样，并且还需要pre_cur表示当前节点的前驱节点，因为prev每次进入一个新的
        子树时都会更新，而我们要求pre_cur是在每次比较时都指向该节点之前的那个点。
        此外这里不能找到两个逆序对之后提前结束，因为Morris算法对树结构有修改，必须等算法全部结束对树结构进行恢复。这也导致了在这里
        运行时间较慢。
        """
        if not root:
            return
        cur = root
        swap1, swap2 = None, None
        pre_cur = None
        while cur:
            if not cur.left:
                # print(cur.val)
                if pre_cur and pre_cur.val > cur.val:
                    if not swap1 and not swap2:
                        swap1 = pre_cur
                        swap2 = cur
                    else:
                        swap2 = cur
                        break
                pre_cur = cur
                cur = cur.right
            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right
                if not prev.right:
                    prev.right = cur
                    cur = cur.left
                else:
                    # print(cur.val)
                    if pre_cur and pre_cur.val > cur.val:
                        if not swap1 and not swap2:
                            swap1 = pre_cur, swap2 = cur
                        else:
                            swap2 = cur
                            break
                    prev.right = None
                    pre_cur = cur
                    cur = cur.right
        swap1.val, swap2.val = swap2.val, swap1.val


t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t1.left = t3
t3.right = t2
# t4.left = t2
s = Solution()
s.recoverTree(t1)
