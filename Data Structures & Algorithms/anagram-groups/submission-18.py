class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagramMap={}

        for i in range(len(strs)):
                sorted_s= "".join(sorted(strs[i]))
                if sorted_s in anagramMap:
                    anagramMap[sorted_s].append(strs[i])
                else:
                    anagramMap[sorted_s]=[strs[i]] 

        output=[]
        for value in anagramMap.values():
            output.append(value)     
        return output