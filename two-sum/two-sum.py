class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #Creating HashMap ie. value:index
        
        for i,val in enumerate(nums): #Where We Used i as iterator (index), val for (value)
            diff = target - val #trying to find out the difference
            
            #If Diff Exists we return it in form of list as [1,2] 
            #where first is difference from hashmap and another is current index 
            if diff in prevMap:
                return [prevMap[diff],i]
            
            prevMap[val]=i #Updating HashMap If diff not found 
        return