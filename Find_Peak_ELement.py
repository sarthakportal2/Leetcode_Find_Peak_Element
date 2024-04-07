class Solution:
     def findPeakElement(self, nums: List[int]) -> int:
        #T(C(N)=O(N)) and S(C(N)=O(1)) as it requires non additional space iteratively
        #Binary Search alg
        l,h=0,len(nums)-1#initializing the low and end pointer
        while l<h:#iterating from low to high 
            mid=(l+h)//2#mid val calculation
            if nums[mid]<nums[mid+1]:l=mid+1#low val calcultation to mid's next current pos
            else:h=mid #mid val declare to it s high val 
            
        return l #printing low 
