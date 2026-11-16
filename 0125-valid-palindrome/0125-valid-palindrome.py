class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = "abcdefghijklmnopqrstuvwxyz0123456789"
        s = s.lower()
        clean = ""
        for i in s:
            if i in alphanum:
                clean = clean + i
        if clean == clean[::-1]:     # Or, direct return clean = clean[::-1]:
            return True              # Automatically gets True or False
        else:
            return False