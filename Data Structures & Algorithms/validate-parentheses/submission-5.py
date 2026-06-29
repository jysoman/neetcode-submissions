from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        fifo_queue = deque()
        opened = {"(", "{", "["}
        closed = {")":"(", "}":"{", "]":"["}
        if len(s) < 2:
            return False
        for element in s:
            if element in opened:
                fifo_queue.append(element)
            else:
                #check if it is the closing bracket of the last element
                if not fifo_queue or closed[element] != fifo_queue[-1]:
                    return False
                open_brack = fifo_queue.pop()
            
        if fifo_queue:
            return False
        return True