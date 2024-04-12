import numpy as np
from graph.data_read import read_file

def dijkstra(graph, start, end):
    num_vertices = len(graph)
    distances = [float('inf')] * num_vertices
    distances[start] = 0
    previous_vertices = [-1] * num_vertices
    visited = [False] * num_vertices
    for _ in range(num_vertices):
        min_distance = float('inf')
        current_vertex = -1
        for vertex in range(num_vertices):
            if not visited[vertex] and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                current_vertex = vertex
        visited[current_vertex] = True
        for vertex in range(num_vertices):
            if not visited[vertex] and graph[current_vertex][vertex] != 0:
                new_distance = distances[current_vertex] + graph[current_vertex][vertex]
                if new_distance < distances[vertex]:
                    distances[vertex] = new_distance
                    previous_vertices[vertex] = current_vertex
    path = []
    current_vertex = end
    while current_vertex != -1:
        path.insert(0, current_vertex)
        current_vertex = previous_vertices[current_vertex] 
    return distances[end], path



def dijkstra_file(name, start, end):
    graph, num_vertices = read_file(name)
    distances = [float('inf')] * num_vertices
    distances[start] = 0
    previous_vertices = [-1] * num_vertices
    visited = [False] * num_vertices
    for _ in range(num_vertices):
        min_distance = float('inf')
        current_vertex = -1
        for vertex in range(num_vertices):
            if not visited[vertex] and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                current_vertex = vertex
        visited[current_vertex] = True
        for vertex in range(num_vertices):
            if not visited[vertex] and graph[current_vertex][vertex] != 0:
                new_distance = distances[current_vertex] + graph[current_vertex][vertex]
                if new_distance < distances[vertex]:
                    distances[vertex] = new_distance
                    previous_vertices[vertex] = current_vertex
    path = []
    current_vertex = end
    while current_vertex != -1:
        path.insert(0, current_vertex)
        current_vertex = previous_vertices[current_vertex] 
    return distances[end], path



if __name__ == '__main__':
    graph, n = read_file('data.txt')



    start_vertex = 3
    end_vertex = 0
    distance, path = dijkstra(graph, start_vertex, end_vertex)

    print(f"Минимальное расстояние от вершины {start_vertex} до вершины {end_vertex}: {distance}")
    print(f"Путь: {' -> '.join(map(str, path))}")