class Solution:
    def isPalindrome(self, s: str) -> bool:



        """
        #solution 1 - uses extra memory

        #removing all non-alphanumeric characters aka spaces
        newString = ""


        for c in s:
            if c.isalnum():
                newString += c.lower()


        return newString == newString[::-1]

        """


        """
        use pointers - increase left pointer, decrement pointer, till meet in the middle or both pass each other

        using ascii values if the char is alphanumeric or not

        """
        left, right, = 0, len(s) - 1

        #havent met or crossed each other yet
        while left < right: 

            #make sures both characters are alphanumeric
            while left < right and not self.alphaNum(s[left]):
                left += 1

            while right > left and not self.alphaNum(s[right]):
                right -= 1


            if s[left].lower() != s[right].lower():
                return False
            
            left, right = left + 1, right - 1
        return True


    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord ('Z')
        or ord('a') <= ord(c) <= ord ('z') or
        ord('0') <= ord(c) <= ord ('9'))

        