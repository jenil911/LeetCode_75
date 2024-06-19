class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Find the maximum number of candies any kid currently has
        maxCandies = max(candies)
        
        # List to store results
        greatestCandies = []
        
        # Check each kid's candies after adding extraCandies
        for candy in candies:
            greatestCandies.append(candy + extraCandies >= maxCandies)
        
        return greatestCandies