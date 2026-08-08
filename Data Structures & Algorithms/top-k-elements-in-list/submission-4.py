class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        get a count of all elements in a hash map num2freq
        reverse the hash map freq2num
        get all the keys of the freq2num, sort and pick top k from freq2num

        """

        num2freq = {}
        for num in nums:
            if num not in num2freq:
                num2freq[num] = 1
            else:
                num2freq[num] += 1

        freq2num = {}
        for num,freq in num2freq.items():
            if freq in freq2num:
                freq2num[freq].append(num)
            else:
                freq2num[freq] = [num]
        poss = list(freq2num.keys())
        poss.sort(reverse=True)
        topk_keys = poss[:k]

        topkeys = []
        for key in topk_keys:
            topkeys.extend(freq2num[key])
            if len(topkeys) >= k:
                break
        return topkeys[:k]