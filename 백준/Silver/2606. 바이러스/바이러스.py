from collections import deque

n_nodes = int(input())
n_edges = int(input())
graph = [[] for i in range(n_nodes + 1)]
visited = [0] * (n_nodes + 1)

for i in range(n_edges):
   a, b = map(int, input().split())
   graph[a].append(b)
   graph[b].append(a)

visited[1] = 1
q = deque([1])

while q:
   node = q.popleft()
   for next_node in graph[node]:
       if not visited[next_node]:
           q.append(next_node)
           visited[next_node] = 1

print(sum(visited) - 1)