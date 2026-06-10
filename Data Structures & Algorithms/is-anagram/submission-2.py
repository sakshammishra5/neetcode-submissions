class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sorted_s=sorted(s)
        sorted_t=sorted(t)

        if len(sorted_s)==len(sorted_t):
            word_s= "".join(sorted_s)
            word_t= "".join(sorted_t)
            
            for i in range(len(word_s)):
                if word_s[i]!=word_t[i]:
                   return False
            return True
        else:
            return False  