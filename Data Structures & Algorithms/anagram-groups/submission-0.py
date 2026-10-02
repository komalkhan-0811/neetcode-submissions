class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #at most we have 26 characters - since all lowercase
        # use an array to keep the number of each characters it has
        # use a hashmap, and the key woudl be the array and outputs the list that matches with all of those keys

        result = defaultdict(list) # mapping the charCount of each string and mapping that to the list of anagrams

        for s in strs:
            count = [0] * 26 # a - z

            #go through every character in each string and count how many of each character

            for c in s:
                count[ord(c) - ord("a")] += 1

            
            result[tuple(count)].append(s)

        return list(result.values())