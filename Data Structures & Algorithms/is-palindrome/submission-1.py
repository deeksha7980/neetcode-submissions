class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace(" ",'').lower()
        sl=list(filter(str.isalnum, s))
        if sl==sl[::-1]:
            return True
        else:
            return False
        