class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a hashmap
        freq_map={}
        for num in nums:
            if num in freq_map:
                freq_map[num]+=1
            else:
                freq_map[num]=1
         
    #  create a bucket array for the hashmap
        bucket=[[] for _ in range(len(nums)+1)]

    # place the numbers into their frequency array
        for num,freq in freq_map.items():
             bucket[freq].append(num)
    
      #collect top k element from the highest frequency
        res=[]
        for i in range(len(bucket)-1,0,-1):
            for n in bucket[i]:
                res.append(n)
                if len(res)==k:
                   return res
        return res            


        