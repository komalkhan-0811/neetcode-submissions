class Solution:
    def findMin(self, nums: List[int]) -> int:
        # ---- QUICK ANALYSIS -------
        # let's take [3,4,5,6,1,2]
        # mid = 3+2 // 2 = 2
        # nums[2] = 5 --> which side of the array are we in ? 
        # we have a left pointer initialized at 0 and right pointer at the end
        # nums[left] = 3 and nums[right] = 2
        # nums[right] < nums[mid] so we're on the left portion of the array and we need to search the right portion to find the minimum

        # -------------------------------
        res = nums[0]
        left = 0
        right = len(nums)-1
        while left <= right:
            if nums[left] < nums[right]: # edge case where the array hasn't rotated or has rotated n times and is back to its original state
                res = min(res, nums[left])
                break
            mid = (left+right)//2
            res = min(nums[mid], res)
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return res
