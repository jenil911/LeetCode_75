class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into words using whitespace as delimiter
        words = s.split()
        
        # Reverse the order of words
        words.reverse()
        
        # Join the reversed words with a single space as separator
        return ' '.join(words)