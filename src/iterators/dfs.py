class Graph:
    def __init__(self, edges: list[tuple[int, int]]):
        self.edges = edges
        self.vertices = []
        for edge in edges:
            if edge[0] not in self.vertices:
                self.vertices.append(edge[0])
            if edge[1] not in self.vertices:
                self.vertices.append(edge[1])

    def dfs(self) -> list[int]:
        """Depth-first search algorithm. Returns list of visited vertices."""
        vertices_state = {
            "white": self.vertices.copy(),
            "gray": list(),
            "black": list(),
        }
        visited_vertices_list = []

        def dfs_step(vertex):
            if vertex in vertices_state["white"]:
                visited_vertices_list.append(vertex)
                vertices_state["white"].remove(vertex)
                vertices_state["gray"].append(vertex)

                for edge in self.edges:
                    if edge[0] == vertex:
                        dfs_step(edge[1])
                    if edge[1] == vertex:
                        dfs_step(edge[0])

                vertices_state["gray"].remove(vertex)
                vertices_state["black"].append(vertex)

        for vertex in self.vertices:
            dfs_step(vertex)

        return visited_vertices_list

    def __iter__(self):
        return _GraphIterable(self.dfs())


class _GraphIterable:
    def __init__(self, dfs_vertices_list):
        self.dfs_vertices_list = dfs_vertices_list
        self.index = 0

    def __next__(self):
        if self.index < len(self.dfs_vertices_list):
            self.index += 1
            return self.dfs_vertices_list[self.index - 1]
        raise StopIteration
