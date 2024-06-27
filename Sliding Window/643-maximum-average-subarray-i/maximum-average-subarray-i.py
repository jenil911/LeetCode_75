class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Calculate the sum of the first k elements
        max_sum = cur = sum(nums[:k])
        
        # Slide the window across the array
        for i in range(len(nums) - k):
            # Update the current sum by subtracting the element that goes out of the window
            # and adding the new element that comes into the window
            cur = cur - nums[i] + nums[i + k]
            
            # Update max_sum if the new current sum is larger
            if cur > max_sum:
                max_sum = cur
        
        # Calculate the maximum average
        return max_sum / k