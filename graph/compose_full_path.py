import numpy as np
from graph.new_d import dijkstra
from graph.data_read import read_file
from graph.extra_vertexes import add_vertices



def compose_full_path(start_vertex: int = 3, end_vertex: int = 0, name:str =  './graph/data.txt'):

    graph, n = read_file(name)
    distance, path = dijkstra(graph, start_vertex, end_vertex)
    # print(f"Минимальное расстояние от вершины {start_vertex} до вершины {end_vertex}: {distance}")
    tmp_path = list(map(str, path))
    final_path = add_vertices(tmp_path)
    return final_path

# print(compose_new_path())