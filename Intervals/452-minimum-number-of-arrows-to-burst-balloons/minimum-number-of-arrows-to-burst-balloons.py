class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        current_shot_x = points[0][1]
        res = 1
        for i in range(1, len(points)):
            if points[i][0] > current_shot_x:
                current_shot_x = points[i][1]
                res += 1
        return res