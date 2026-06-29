from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        lifo_queue = []
        closed = {")":"(", "}":"{", "]":"["}

        for element in s:
            if element in closed:
                if lifo_queue and closed[element] == lifo_queue[-1]:
                    lifo_queue.pop()
                else:
                    return False
            else:
                lifo_queue.append(element)
            
        return True if not lifo_queue else False