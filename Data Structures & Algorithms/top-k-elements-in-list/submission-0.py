from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map=Counter(nums) #create a freq hash map

        sorted_freq=sorted(freq_map.keys(),key=lambda x:freq_map[x],reverse=True)


        return sorted_freq[:k] 

        