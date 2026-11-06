class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        b_arr = [[] for i in range(len(nums) + 1)]
        freq=defaultdict(int)
        for num in nums:
            freq[num]+=1
        for f in freq:
            b_arr[freq[f]].append(f)
        res=[]
        for i in range(len(nums),0,-1):
            for num in b_arr[i]:
                res.append(num)
                if len(res)==k:
                    return res


        