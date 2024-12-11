def dfs(G, visited, s):
    stack = [s]
    cc = []  # We'll store connected nodes here
    visited[s] = True  # Mark the starting node as visited
    while stack:
        v = stack.pop()
        cc.append(v)
        for u in G[v]:
            if not visited[u]:
                visited[u] = True
                stack.append(u)
    return cc


def connected_components(G):
    visited = [False] * len(G)
    conn_comp = []  # List to store all connected components
    for i in range(len(G)):
        if not visited[i]:
            cc = dfs(G, visited, i)
            conn_comp.append(cc)  # Add connected component
    return len(conn_comp), conn_comp


if __name__ == '__main__':
    N, M = map(int, input().split())  # Number of vertices and edges
    G = [[] for _ in range(N)]  # Initialize adjacency list for the graph
    for _ in range(M):
        v1, v2 = map(int, input().split())  # Read edges
        G[v1].append(v2)
        G[v2].append(v1)

    n_comp, conn_comp = connected_components(G)
    print(n_comp)  # Print the number of connected components
    for cc in conn_comp:
        print(len(cc))  # Print the size of each connected component
        print(
            ' '.join(map(str, sorted(cc))))  # Print the nodes in the connected component, sorted for consistent output
