from iterators.dfs import Graph
from random import randint


def test_method_simple():
    graph = Graph([(1, 2), (2, 4), (5, 3)])
    assert graph.dfs() == [1, 2, 4, 5, 3]


def test_iterator_simple():
    graph = Graph([(1, 2), (2, 4), (5, 3)])
    assert list(graph) == [1, 2, 4, 5, 3]


def test_method_zero_elements():
    graph = Graph([])
    assert graph.dfs() == []


def test_iterator_zero_elements():
    graph = Graph([])
    assert list(graph) == []


def test_method_edge_to_same_element():
    graph = Graph([(1, 2), (2, 4), (3, 3)])
    assert graph.dfs() == [1, 2, 4, 3]


def test_iterator_edge_to_same_element():
    graph = Graph([(1, 2), (2, 4), (3, 3)])
    assert list(graph) == [1, 2, 4, 3]


def test_iterator_possibility_of_parallel_working():
    graph = Graph([(1, 2), (2, 4)])
    result = []
    for i in graph:
        for j in graph:
            result.append((i, j))
    assert result == [
        (1, 1),
        (1, 2),
        (1, 4),
        (2, 1),
        (2, 2),
        (2, 4),
        (4, 1),
        (4, 2),
        (4, 4),
    ]


def test_random_correct_vertices():
    random_edges = [
        (randint(-1000, 1000), randint(-1000, 1000)) for _ in range(randint(1, 1000))
    ]
    random_edges_vertices_set = set()
    for edge in random_edges:
        random_edges_vertices_set.add(edge[0])
        random_edges_vertices_set.add(edge[1])
    graph = Graph(random_edges)
    assert sorted(graph.dfs()) == sorted(random_edges_vertices_set)
