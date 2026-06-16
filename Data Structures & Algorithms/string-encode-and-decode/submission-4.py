class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=""
        for i in range(len(strs)):
            length=len(strs[i])
            encoded_string+=str(length)+":"+strs[i]
        return encoded_string


    def decode(self, s: str) -> List[str]:
        
        decoded_array=[]
        while s:
            colon_index=s.find(":")
            length=int(s[:colon_index])
            start=colon_index+1
            end=start+length
            word=s[start:end]
            decoded_array.append(word)
            s=s[end:]

        return decoded_array
