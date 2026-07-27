class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = {}
        for i in nums:
            f[i] = f.get(i, 0) + 1
            
        l = []
   
        for _ in range(k):
            most_frequent_key = max(f, key=f.get)
            l.append(most_frequent_key)
            f.pop(most_frequent_key) 
            
        return l



    
        