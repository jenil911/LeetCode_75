class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        first = float('inf')
        second = float('inf')
        
        for n in nums:
            if n <= first:
                first = n  # smallest so far
            elif n <= second:
                second = n  # second smallest
            else:
                return True  # found a triplet
        
        return False