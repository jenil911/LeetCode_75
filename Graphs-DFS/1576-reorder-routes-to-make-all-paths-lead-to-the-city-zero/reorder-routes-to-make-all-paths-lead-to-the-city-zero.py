class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        s = 0
        # create dictionary mapping vertices to their adjacent edges
        adj = defaultdict(list)
        for c in connections:
            adj[c[0]].append(c)
            adj[c[1]].append(c)

        # run the search
        curr = seen = {0}
        while curr:
            new = set()  # will contain neighbors of `curr` not in `seen`
            for v in curr:
                for e in adj[v]:
                    if e[0] not in seen and e[1] == v:
                        # pointing the 'right' direction
                        new.add(e[0])
                    elif e[0] == v and e[1] not in seen:
                        # pointing the 'wrong' direction
                        new.add(e[1])
                        s += 1
            curr = new
            seen.update(new)

        return s