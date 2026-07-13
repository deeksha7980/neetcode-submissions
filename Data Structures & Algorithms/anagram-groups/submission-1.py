from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        li = []  # list of groups
        used = [False] * len(strs)  # track words by index instead of value

        for i in range(len(strs)):
            if used[i]:
                continue
            group = [strs[i]]
            used[i] = True
            for j in range(i + 1, len(strs)):
                if not used[j] and sorted(strs[i]) == sorted(strs[j]):
                    group.append(strs[j])
                    used[j] = True
            li.append(group)

        return li
