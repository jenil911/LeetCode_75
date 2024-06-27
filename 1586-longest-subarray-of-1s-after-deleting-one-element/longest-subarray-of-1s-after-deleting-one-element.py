class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        count = 0
        m_size = 0
        for j in range(len(nums)):
            if nums[j]==0: 
                count+=1
            while count > 1:
                if nums[i]==0:
                    count-=1
                i+=1
            m_size = max(m_size,j-i)
        return m_size
                    
        