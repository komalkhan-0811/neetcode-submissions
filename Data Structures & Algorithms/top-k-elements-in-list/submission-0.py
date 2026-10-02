class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hashmap
        count = {}
        #storing the array
        freq = [[] for i in range (len(nums) + 1)] 

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        #going through each value that we have counted
        for n, c in count.items(): #returns every single key value pair we've added to dict
            #count is the index and the value would be that list that occured index amount of itme 
            freq[c].append(n)


        result = []
        for i in range (len(freq) -1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
        