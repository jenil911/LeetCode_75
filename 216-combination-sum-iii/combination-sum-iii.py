class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return [
            x
            for x in [
                reduce(lambda x, y: x + y, s)
                for s in product(*[[[], [i]] for i in range(1, 10)])
            ]
            if len(x) == k and sum(x) == n
        ]