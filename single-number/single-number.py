class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        #Using Bit Manipulation
        a = 0
        for i in nums :
            a ^= i 
        return a
        
#         Using Extra Space Memory (i.e Python Dictionaries)
#         counts = {}
        
#         for n in nums:
#             if n not in counts:
#                 counts[n] = 1
#             else:
#                 del counts[n]  
#         return list(counts.keys())[0]