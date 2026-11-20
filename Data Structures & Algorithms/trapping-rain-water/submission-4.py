class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        maxL=height[l]
        maxR=height[r]
        totW=0
        while (l<r):
            maxL,maxR=max(maxL,height[l]),max(maxR,height[r])
            if (maxL<=maxR):
                tempW=min(maxL,maxR)-height[l]
                l+=1
            else :
                tempW=min(maxL,maxR)-height[r]
                r-=1
            if (tempW>0):
                totW+=tempW
        return totW