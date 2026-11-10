class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j=0,len(heights)-1
        maxArea=0
        while (i<j):
            width,height=j-i,min(heights[i],heights[j])
            tempArea=width*height
            if maxArea<(tempArea):
                maxArea=tempArea
            
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return maxArea