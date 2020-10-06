#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/9/3 16:24
# @Author:JiahangGu

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        """
        初始想法：从根节点开始，每个节点可以选择偷或者不偷，并且需要传递一个标志位，如果父节点偷了，那么子节点就不能偷。
        最终记录到达叶子节点的最大值即可。
        观察示例发现一处问题：可以多条路径偷，而不是从根节点到叶子节点这一条路径里。那这其实就是层次遍历的解决方案，计算出
        所有间隔层次的最大和即可。
        解法选用BFS获得层次遍历序列，然后求解隔行的最大和。
        :param root:
        :return:
        """
        # q = [root]
        # level = []
        # cur_level = []
        # cur_level_num = 1
        # next_level_num = 0
        # while q:
        #     node = q.pop(0)
        #     cur_level.append(node.val)
        #     if node.left:
        #         next_level_num += 1
        #         q.append(node.left)
        #     if node.right:
        #         next_level_num += 1
        #         q.append(node.right)
        #     cur_level_num -= 1
        #     if cur_level_num == 0:
        #         level.append(cur_level)
        #         cur_level = []
        #         cur_level_num = next_level_num
        #         next_level_num = 0
        # odd_sum, even_sum = 0, 0
        # for i in range(len(level)):
        #     if i & 1 == 0:
        #         even_sum = sum(level[i])
        #     else:
        #         odd_sum = sum(level[i])
        # return max(even_sum, odd_sum)
        """
        好吧，又一次被示例骗了，和层次遍历关系不大，例如单链结构的数4123，最终结果是43而不是42，不过好在复习了一边层次遍历不亏
        有了上述尝试后，在根据题目的情况，在树中给定特定条件求出极值，这不就是树形DP吗？（虽然我不会，但是我看到题解了。。），又
        可以学习新知识了。
        树形DP介绍见DP文件夹下文档
        首先是暴力解法：当前根节点的值怎么计算呢？首先如果选择这个根节点，那么左右子节点就不能选择，但是这不影响孙子节点的选择，
        于是问题变为孙子节点的最大值，可见这是一个重复子结构问题。如果不选择根节点，那么最大值就是左右子节点的最大值的和，而他们
        的最大值又取决于以他们为根节点的子数的最大值，依旧是重复子结构问题。所以问题可以很明显的得到如下公式;
        if 选择根节点：max_value = 根节点的值+所有孙子节点的值
        else: max_value = 左右子节点的值的和
        """
        # def dfs(node):
        #     if not node:
        #         return 0
        #     cur_money = node.val
        #     if node.left:
        #         cur_money += dfs(node.left.left)
        #         cur_money += dfs(node.left.right)
        #     if node.right:
        #         cur_money += dfs(node.right.left)
        #         cur_money += dfs(node.right.left)
        #     return max(cur_money, dfs(node.left) + dfs(node.right))
        # return dfs(root)
        """
        暴力法在py实现超时，因为其中的重复子结构计算了很多次，比如计算当前节点的值时，需要用到儿子节点的值和孙子节点的值，
        而在计算儿子节点时还需要计算孙子节点的值，这就导致了重复计算。可以使用记忆化搜索的方法来进行改进，即记录每个节点的
        最大值，在访问到的时候直接取出来即可。时间复杂度为O(n)，每个节点只需要求一次即可。
        """
        # def dfs(node):
        #     if not node:
        #         return 0
        #     if value_dict.get(id(node), -1) != -1:
        #         return value_dict[id(node)]
        #     cur_money = node.val
        #     if node.left:
        #         cur_money += dfs(node.left.left)
        #         cur_money += dfs(node.left.right)
        #     if node.right:
        #         cur_money += dfs(node.right.left)
        #         cur_money += dfs(node.right.right)
        #     value = max(cur_money, dfs(node.left) + dfs(node.right))
        #     value_dict[id(node)] = value
        #     return value
        #
        # value_dict = dict()
        # return dfs(root)
        """
        成功通过，但是这个还有进一步优化空间和时间常数的方法。记录当前节点选和不选左右子节点的最优值，则结果是
        max(根节点+不选左右子节点的值， 左右子节点的值）
        """
        def dfs(node):
            """
            返回当前根节点选择和不选择的最大值。如果选择该节点，最大值为左侧公式，表示再选择左右子节点均不选择所能得到的
            最大值，而不选择该节点，最大值为右侧公式，表示左右子节点所能得到的最大值，而左右子节点是否选择又取决于其自身
            作为根节点时的结果，并且选或不选都有可能达到最大值的解，所以要返回其中最大的结果。这样就避免了上述重复子结构
            造成的重复计算导致的超时问题。
            :param node:
            :return:
            """
            if not node:
                return 0, 0
            left_choose, left_not_choose = dfs(node.left)
            right_choose, right_not_choose = dfs(node.right)
            not_choose = max(left_choose, left_not_choose) + max(right_choose, right_not_choose)
            return node.val + left_not_choose + right_not_choose, not_choose

        return max(dfs(root))


s = Solution()
print(s.rob())
