class Solution:
    def minDominoRotations(self, tops:, bottoms):
        
        for x in [tops[0] , bottoms[0]]:  # Try both first elements as candidates
            top_swap , bottom_swap = 0,0
            
            for i in range(len(tops)):
                # If x not found in either, skip candidate
                if tops[i] != x and bottoms[i] != x:
                    break
                if tops[i] != x:
                    top_swap +=1  # Increment top swap if top doesn't match
                if bottoms[i] != x:
                    bottom_swap +=1  # Increment bottom swap if bottom doesn't match
            else:
                return min(top_swap , bottom_swap)  # Valid candidate found
        
        return -1  # No candidate worked