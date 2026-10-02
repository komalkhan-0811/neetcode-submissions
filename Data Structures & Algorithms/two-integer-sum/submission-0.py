class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # start with the first indice - less than target - great
        # you keep the first index and traverse thru the array to see whether that index 1 + next possible index = target

        # optimal solution with the correct time complexity is hashmap
        # because with the initial idea, that would have been 2 nested for loops which would have been O(n^2) which is not optimal
        # using the complement idea would easily check if we have that number in the hashmap or not

# i is the index and num is the value 
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]

            # If the complement wasn't found, store the current number and its index, so future numbers can check against i
            seen[num] = i

        return []

        




