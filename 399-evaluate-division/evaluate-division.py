class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Build the graph
        graph = {}
        for (a, b), value in zip(equations, values):
            if a not in graph:
                graph[a] = {}
            if b not in graph:
                graph[b] = {}
            graph[a][b] = value
            graph[b][a] = 1 / value

        def dfs(src: str, dst: str, visited: Set[str]) -> float:
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0
            visited.add(src)
            for neighbor, value in graph[src].items():
                if neighbor in visited:
                    continue
                result = dfs(neighbor, dst, visited)
                if result != -1.0:
                    return result * value
            return -1.0

        results = []
        for query in queries:
            results.append(dfs(query[0], query[1], set()))
        return results