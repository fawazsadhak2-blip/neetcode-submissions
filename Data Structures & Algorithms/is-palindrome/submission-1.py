class Solution:
    def isPalindrome(self, s: str) -> bool:
        new=""
        x=s.lower()
        for i in x:
            if i.isalnum():
                new+=i
                
        return new==new[::-1]
        