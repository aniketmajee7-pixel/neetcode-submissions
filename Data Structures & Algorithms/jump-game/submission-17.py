class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size=len(nums)
        i=0
        while(i+nums[i]<size-1):
            max_reach=i+nums[i]
            index=i
            for j in range(nums[i]):
                k=i+j+1
                if k+nums[k]>max_reach:
                    max_reach=k+nums[k]
                    index=k
            if index==i:
                return False
            i=index
        return True
                
    

        
