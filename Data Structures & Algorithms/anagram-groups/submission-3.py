class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        res = []
        for word in strs:
            sorted_word = "".join(sorted(word))
            seen[sorted_word].append(word)
        
        for key, val in seen.items():
            res.append(val)
        return res