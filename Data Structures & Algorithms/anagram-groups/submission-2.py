class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for word in strs:
            sorted_s = "".join(sorted(word))
            seen[sorted_s].append(word)
            
        return list(seen.values())