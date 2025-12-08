import itertools
import math
import networkx as nx


def part_1(lines: list[str]) -> str | int:
    graph, sorted_edges = _get_graph_and_sorted_edges(lines)

    # Limit number of initial edges when using min input
    num_edges = 1000 if len(lines) > 100 else 10
    graph.add_edges_from(sorted_edges[:num_edges])

    sorted_components = sorted(nx.connected_components(graph), key=len, reverse=True)
    return math.prod(len(component) for component in sorted_components[:3])


def part_2(lines: list[str]) -> str | int:
    graph, sorted_edges = _get_graph_and_sorted_edges(lines)

    for edge in sorted_edges:
        graph.add_edge(*edge)
        if nx.is_connected(graph):
            return edge[0][0] * edge[1][0]

    raise RuntimeError("No solution found")


def _get_graph_and_sorted_edges(lines):
    points = {tuple(map(int, line.split(","))) for line in lines}

    graph = nx.Graph()
    graph.add_nodes_from(points)

    return graph, _get_sorted_edges(points)


def _get_sorted_edges(points):
    weighted_edges = []

    for p, q in itertools.combinations(points, 2):
        weighted_edges.append((
            (p, q),
            math.dist(p, q)
        ))

    return [edge for edge, _ in sorted(weighted_edges, key=lambda x: x[1])]