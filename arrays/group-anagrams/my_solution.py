from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:



        hmap = {}
        res = []

        for i in range(len(strs)):

            sort_s = tuple(sorted(strs[i]))

            if sort_s not in  hmap:
                hmap[sort_s] = [strs[i]]
            else:
                hmap[sort_s].append(strs[i])

        for  v in hmap.values():
            res.append(v)

        return res
