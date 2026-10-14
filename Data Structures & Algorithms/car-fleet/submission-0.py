class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s = len(position)
        time = dict({})
        
        for i in range(s):
            time[position[i]] = (target - position[i]) / speed[i]
        
        position.sort(reverse = True)
        stack = []

        for i in position:
            stack.append(time[i])
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

        