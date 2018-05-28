class Graph:
    class Node:
        def __init__(self, name, value):
            self.name = name
            self.value = value

    def __init__(self):
        self.adj_list = {}

    def add_node(self, node_name, value):
        temp = self.Node(value)
        self.adj_list[node_name] = temp

    def link_node(self, a, b):
        self.adj_list[a].append(b)

    # breadth first search
    def bfs(self):
        pass

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

 '''
    a---b
    \    \
     \    e
      \    \
      d---c

     adj_list = {
                a: [b,d],
                b: [a,e],
                c: [e,d],
                d: [a,c],
                e: [b,c],
            }
    GRAPH_OBJECT.get_path(a,c)
    ->
        one out of following two:
            1. [a, d, c]
            2. [a, b, e, c]
    ->

'''
