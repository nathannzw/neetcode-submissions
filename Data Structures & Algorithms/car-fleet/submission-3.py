# STACK SOLUTION
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list(zip(position, speed))
        pair.sort(reverse=True)

        stack = []
        for p, s in pair:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)



'''
# ITERATIVE SOLUTION
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list(zip(position, speed))
        pair.sort(reverse=True)

        fleets = 1
        previous_time = (target - pair[0][0]) / pair[0][1] # time = distance / speed
        for i in range(1, len(pair)):
            current_car = pair[i]
            current_time = (target - current_car[0]) / current_car[1]
            if current_time > previous_time:
                fleets += 1
                previous_time = current_time

        return fleets

'''