class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        

        hm = {}

        for ele in grid:
            ele = tuple(ele)
            if(ele not in hm):
                hm[ele]=1
            else:
                hm[ele]+=1
        result = 0
        print(hm)
        for i in range(len(grid[0])):
            temp = []
            for j in range(len(grid[0])):
                temp.append(grid[j][i])
            print(temp,"temp")
            if(hm.get(tuple(temp))!=None):
                result+= hm.get(tuple(temp))
        return result