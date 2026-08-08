class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        create a hashmap of key as sorted chars and value as the str that matches the letters
        iterate over strs, add to hashmap
        return values
        """

        anagrams = {}
        for str_i in strs:
            sorted_str = "".join(sorted(str_i))
            if sorted_str in anagrams:
                anagrams[sorted_str].append(str_i)
            else:
                anagrams[sorted_str] = [str_i]

        return list(anagrams.values())