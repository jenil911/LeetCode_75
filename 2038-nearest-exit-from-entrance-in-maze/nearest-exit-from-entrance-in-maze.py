class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m,n=len(maze),len(maze[0])
        visited=[[0 for i in range(n)] for j in range(m)]
        l=deque([(*entrance,0)])
        visited[entrance[0]][entrance[1]]=1
        while len(l)>0:
            x,y,depth=l.popleft()
            for i,j in [(x-1,y),(x+1,y),(x,y-1),(x,y+1),]:
                if i>=0 and i<m and j>=0 and j<n and visited[i][j]==0 and maze[i][j]!='+': 
                    if (i==0 or i==m-1 or j==0 or j==n-1) and not (i==entrance[0] and j==entrance[1]): return depth+1
                    l.append((i,j,depth+1))
                    visited[i][j]=1
        return -1