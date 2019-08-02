import sys

class Graph:
    def __init__(self, num_v):
        self.num_v = num_v
        self.graph = [[0 for _ in range(num_v)]
                        for __ in range(num_v)]

    
    def find_shortest_path_in_step(self, isShortest, distances):
        min_dist = sys.maxsize
        for idx, dist in enumerate(distances):
            if min_dist > dist and not isShortest[idx]:
                min_dist = dist
                idx_pick = idx
        return idx_pick
    
    def dijkstra(self, src):
        isShortest = [False] * self.num_v
        distances = [sys.maxsize] * self.num_v
        shortest_path = [[src]]*self.num_v
        distances[src] = 0
        for _ in range(self.num_v):
            idx_pick = self.find_shortest_path_in_step(isShortest, distances)
            isShortest[idx_pick] = True
            for v in range(self.num_v):
                if self.graph[idx_pick][v] > 0 and \
                (distances[idx_pick] + self.graph[idx_pick][v]) < distances[v] and \
                not isShortest[v]:
                    distances[v] = distances[idx_pick] + self.graph[idx_pick][v]
                    shortest_path[v] = shortest_path[idx_pick].copy()
                    shortest_path[v].append(v)
        return distances, shortest_path

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
           [4, 0, 8, 0, 0, 0, 0, 11, 0], 
           [0, 8, 0, 7, 0, 4, 0, 0, 2], 
           [0, 0, 7, 0, 9, 14, 0, 0, 0], 
           [0, 0, 0, 9, 0, 10, 0, 0, 0], 
           [0, 0, 4, 14, 10, 0, 2, 0, 0], 
           [0, 0, 0, 0, 0, 2, 0, 1, 6], 
           [8, 11, 0, 0, 0, 0, 1, 0, 7], 
           [0, 0, 2, 0, 0, 0, 6, 7, 0] 
          ]; 

distances, shortest_path = g.dijkstra(0)
print(distances)
print(shortest_path)