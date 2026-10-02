class Solution:

    def encode(self, strs: List[str]) -> str:

        result = ""

        for s in strs:
            #len s is basically the integer that will be in front of the word then add a # as the delimiter 
            result += str(len(s)) + "#" + s

        return result

    def decode(self, s: str) -> List[str]:
        #need to return back the og set of strings 
        # i is a pointer which tells us which position we are at the input string so far
        result, i = [], 0

        #each iteration of this loop reads one entire word
        #read character by character
        while i < len(s):
            #first position is an integer
            # have a second pointer j looking for the delimiter
            j = i
            while s[j] != "#":
                j += 1

            #once reached the delimiter then you know the lnght of that string based off of index i
            length = int(s[i:j]) #this is the integer part of the string

            result.append(s[j + 1: j + 1 + length])
            i = j + 1 + length

        return result

