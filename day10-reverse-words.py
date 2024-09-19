class Solution:
    #Function to reverse words in a given string.
    def reverseWords(self,s):
        # code here
        x = s.split('.')
        x = x[::-1]
        s= "."
        z = s.join(x)
        return z
