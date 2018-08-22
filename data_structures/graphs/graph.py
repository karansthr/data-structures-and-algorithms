from collections import Defaultdict


class Graph:

    class Node:
        def __init__(self, name, value):
            self.name = name
            self.value = value

    def __init__(self):
        self.adj_list = Defaultdict(list)

    def add_node(self, node_name):
        self.adj_list[node_name] = []

    def link_node(self, a, b):
        self.adj_list[a].append(b)
        self.adj_list[b].append(a)

    # breadth first search
    def bfs(self):
        start = self.adj_list.keys()[0]
        queue = self.adj_list[start]
        visited = [start]
        while
    # depth first search
    def dfs(self):
        pass

    # get the path from <a> to <b>, path may or may not be optimal
    def get_path(self, a, b):
        stack = [*self.adj_list[a]]
        path = []
        while not stack:
            pass
        return path
