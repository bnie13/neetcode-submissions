class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        length = len(s)
        for i in range(length//2):
            if s[i] != s[length-1-i]:
                return False
        return True


        