class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for str_i in strs:
            sortedstri = "".join(sorted(str_i))
            if sortedstri in output:
                output[sortedstri].append(str_i)
            else:
                output[sortedstri] = [str_i]

        return list(output.values())