class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        m=len(s2)

        if n>m:
            return False

        s1_count=[0]*26
        window_count=[0]*26

        # window ke liye check karenge
        for i in range(n):
            s1_count[ord(s1[i])-ord('a')]+=1
            window_count[ord(s2[i])-ord('a')]+=1
        
        # check if first window is equal
        if(s1_count==window_count):
            return True
        
        for i in range(n,m):
            # naya character ko window mein add karenge
            window_count[ord(s2[i])-ord('a')]+=1

            #purane character ko window se remove karnge
            window_count[ord(s2[i-n])-ord('a')]-=1

            # check karenge har frame(window ke liye) [##] 
            if s1_count==window_count:
                return True
        
        return False


        
        