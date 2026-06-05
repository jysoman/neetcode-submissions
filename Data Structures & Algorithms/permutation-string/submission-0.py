class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen1, seen2 = {}, {}
        window = len(s1)

        for c in s1:
            seen1[c] = 1 + seen1.get(c,0)
        
        if len(s2) < len(s1):
            return False
        
        l,r = 0,0

        while r < len(s2):
            seen2[s2[r]] = 1 + seen2.get(s2[r],0)
            if (r-l+1) > window:
                seen2[s2[l]]-=1
                if seen2[s2[l]] == 0:
                    del seen2[s2[l]]
                l+=1
            if seen2==seen1:
                return True
            r+=1
        return False
