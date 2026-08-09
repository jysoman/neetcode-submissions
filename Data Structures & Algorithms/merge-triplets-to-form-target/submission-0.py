class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid_a = valid_b = valid_c = False
        max_a = target[0] 
        max_b = target[1] 
        max_c = target[2]

        for triplet in triplets:
            if triplet[0] > max_a or triplet[1] > max_b or triplet[2] > max_c:
                continue
            if not valid_a and triplet[0] == max_a:
                valid_a = True
            if not valid_b and triplet[1] == max_b:
                valid_b = True
            if not valid_c and triplet[2] == max_c:
                valid_c = True

        return valid_a and valid_b and valid_c