class Solution:
    def isPalindrome(self, s: str) -> bool:

        #solution 1

        #removing all non-alphanumeric characters aka spaces
        newString = ""


        for c in s:
            if c.isalnum():
                newString += c.lower()


        return newString == newString[::-1]


        