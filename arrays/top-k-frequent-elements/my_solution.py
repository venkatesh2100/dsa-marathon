from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        hmap = {}
        res = []

        for i in range(len(nums)):

            hmap[nums[i]] = hmap.get(nums[i] , 0) + 1

        sort_hmap = sorted(hmap.items() , key=lambda x:x[1] , reverse=True)
        i = 0
        while k:
            k-=1

            res.append(sort_hmap[i][0])
            i+=1
        return res
