class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
      n = len(isConnected)

      def dfs(i: int):
        # Mark self visited.
        isConnected[i][i] = 0
        # Visit neighbors.
        for j in range(n):
          if isConnected[j][j] and isConnected[i][j]:
            dfs(j)
        
      num = 0
      for i in range(n):
        if isConnected[i][i]:
          num += 1
          dfs(i)
        
      return num
