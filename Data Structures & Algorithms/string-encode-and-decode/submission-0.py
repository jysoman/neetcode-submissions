class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for str_i in strs:
            res.append(f"{len(str_i)}")
            res.append("#")
            res.append(str_i)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+= 1
            str_i_len = int(s[i:j])
            i = j+1
            j = i+str_i_len
            res.append(s[i:j])
            i = j
        return res

