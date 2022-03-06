class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set() #declaring hashset 
        
        for i in nums: #i is iterator 
            if i in hashset: #if i exists in hashset return true 
                return True 
            hashset.add(i) #else add it to hashset
        return False #duplicate not exist return false