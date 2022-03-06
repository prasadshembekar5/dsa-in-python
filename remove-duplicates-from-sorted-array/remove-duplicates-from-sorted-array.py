class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        l = 1 #first value wont be changed as array is sorted so put l and r at 1st pos
        
        #We have taken r and iterated over 1 to len(num) 
        for r in range(1,len(nums)): 
        #If we found current r position different with previous r position 
        #we will put the actual value of r pos to l ptr po and increment left ptr
            if nums[r] != nums[r-1]:
                nums[l]=nums[r]
                l += 1
        return l #Returning the hoe many unique value we seen 