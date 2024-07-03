class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = Counter(tuple(row) for row in grid)

        pair = 0
        for col in zip(*grid):
            pair += rows[col]
        
        return pair

with open("user.out", "w") as f:
    inputs = map(loads, stdin)