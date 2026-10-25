class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned: str = "".join(char for char in s if char.isalnum()).lower()
        return cleaned == cleaned[::-1]