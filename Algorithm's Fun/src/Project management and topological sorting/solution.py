#!/usr/bin/env python
# encoding: utf-8
# @Time:2020/10/27 14:13
# @Author:JiahangGu

from queue import PriorityQueue as pq


# AOV网络顶点定义
class AOVNode:
    def __init__(self, idx=0, name=None, duration=0, in_degree=0, start_time=0, adjacent=0, adjacent_nodes=None):
        # 结点编号
        self.idx = idx
        # 活动名称
        self.name = name
        # 活动持续时间
        self.duration = duration
        # 顶点入度
        self.in_degree = in_degree
        # 活动最早开始时间
        self.start_time = start_time
        # 相邻结点个数
        self.adjacent = adjacent
        # 相邻结点索引列表
        self.adjacent_nodes = adjacent_nodes

    def __lt__(self, other):
        return self.start_time < other.start_time


class Graph:
    def __init__(self, vertex_cnt=0, vertexs=None):
        # 图中顶点个数
        self.vertex_cnt = vertex_cnt
        # 顶点列表
        self.vertexs = vertexs


# 根据AOE网络特点修改数据结构定义，明确体现边的定义
class EdgeNode:
    def __init__(self, vertex_idx=-1, name=None, duration=0):
        # 活动边终点顶点索引
        self.vertex_idx = vertex_idx
        # 活动边的名称
        self.name = name
        # 活动边的持续时间
        self.duration = duration


class VertexNode:
    def __init__(self, est_time=0, lst_time=0, pre_count=0, edges=None):
        # 事件最早开始时间
        self.est_time = est_time
        # 事件最晚开始时间
        self.lst_time = lst_time
        # 活动的前驱结点个数
        self.pre_count = pre_count
        # 相邻的活动边表
        self.edges = edges


class Solution:
    def topological_sort(self, graph):
        q = pq()
        topo_sorted = []
        for i in range(graph.vertex_cnt):
            if graph.vertexs[i].in_degree == 0:
                q.put(graph.vertexs[i])
        while not q.empty():
            node = q.get()
            print(node.idx)
            topo_sorted.append(node.idx)
            for i in range(node.adjacent):
                adjacent_idx = node.adjacent_nodes[i]
                graph.vertexs[adjacent_idx].in_degree -= 1
                if graph.vertexs[adjacent_idx].in_degree == 0:
                    q.put(graph.vertexs[adjacent_idx])
        return topo_sorted if len(topo_sorted) == graph.vertex_cnt else None

    def calc_est(self, graph, topo_sorted):
        """
        此处的graph参数是AOE网络，注意和拓扑排序graph是AOV网络的区别（vertexs是活动，而AOE中vertexs是事件的表）
        :param graph:
        :param topo_sorted:
        :return:
        """
        graph.vertexs[0].est_time = 0
        for node_idx in topo_sorted:
            for edge in graph.vertexs[node_idx].edges:
                vertex_idx = edge.vertex_idx
                # 最早开始时间是所有前驱结点最早开始时间与持续时间的和的最大值，这里node_idx是vertex_idx的前驱
                cur_time = graph.vertexs[node_idx].est_time + edge.duration
                if cur_time > graph.vertexs[vertex_idx].est_time:
                    graph.vertexs[vertex_idx].est_time = cur_time

    def calc_lst(self, graph, topo_sorted):
        graph.vertexs[-1].lst_time = graph.vertexs[-1].est_time
        for node_idx in reversed(topo_sorted):
            for edge in graph.vertexs[node_idx].edges:
                vertex_idx = edge.vertex_idx
                # 最晚开始时间是所有后继结点最晚结束时间与持续时间的差的最小值，这里vertex_idx是node_idx的后继
                cur_time = graph.vertexs[vertex_idx].lst_time - edge.duration
                if cur_time < graph.vertexs[node_idx].lst_time:
                    graph.vertexs[node_idx].lst_time = cur_time

    def calc_key_path(self, graph):
        topo_sorted = self.topological_sort(graph)
        if not topo_sorted:
            return None
        self.calc_est(graph, topo_sorted)
        self.calc_lst(graph, topo_sorted)
        # 活动的最早开始时间就是事件i的最早开始时间，最晚开始时间就是事件j减去活动的持续时间，若相等则是关键路径
        key_path = []
        for node_idx in topo_sorted:
            for edge in graph.vertexs[node_idx].edges:
                vertex_idx = edge.vertex_idx
                if graph.vertexs[node_idx].est_time == graph.vertexs[vertex_idx].lst_time - edge.duration:
                    key_path.append(edge.name)
        return key_path


vertexs = [AOVNode(0, "P1", 8, 0, 0, 2, [2, 6]),
           AOVNode(1, "P2", 5, 0, 0, 2, [2, 4]),
           AOVNode(2, "P3", 6, 2, 0, 1, [3]),
           AOVNode(3, "P4", 4, 1, 0, 2, [5, 8]),
           AOVNode(4, "P5", 7, 1, 0, 1, [5]),
           AOVNode(5, "P6", 7, 2, 0, 0, []),
           AOVNode(6, "P7", 4, 1, 0, 1, [7]),
           AOVNode(7, "P8", 3, 1, 0, 1, [8]),
           AOVNode(8, "P9", 4, 2, 0, 0, [])]
graph = Graph(9, vertexs)
s = Solution()
print(s.topological_sort(graph))
