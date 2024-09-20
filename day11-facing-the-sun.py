class Solution:
    # Returns count buildings that can see sunlight
    def countBuildings(self, height):
        # code here
        if height is None:
            return 0
        m = 0
        c = 0
        for num in height:
            if(num>m):
                m = num
                c += 1
        return c
