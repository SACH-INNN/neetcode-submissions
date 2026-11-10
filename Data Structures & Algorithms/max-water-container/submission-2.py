class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j=0,len(heights)-1
        maxArea=0
        while (i<j):
            width,height=j-i,min(heights[i],heights[j])
            if maxArea<(width*height):
                maxArea=width*height
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return maxArea