class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            add_asteroid = True
            while stack and stack[-1] > 0 and asteroid < 0:
                if stack[-1] < abs(asteroid):
                    stack.pop()
                elif stack[-1] > abs(asteroid):
                    add_asteroid = False
                    break
                else:  
                    stack.pop()
                    add_asteroid = False
                    break
            if add_asteroid:
                stack.append(asteroid)
        return stack