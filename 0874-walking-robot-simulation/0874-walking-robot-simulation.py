class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y = 0, 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direction_index = 0
        max_distance_sq = 0
        obstacle_set = {tuple(obstacle) for obstacle in obstacles}

        for command in commands:
            if command == -1:
                direction_index = (direction_index + 1) % 4
            elif command == -2:
                direction_index = (direction_index - 1) % 4
            else:
                for _ in range(command):
                    dx, dy = directions[direction_index]
                    if (x + dx, y + dy) in obstacle_set:
                        break
                    x, y = x + dx, y + dy
            max_distance_sq = max(max_distance_sq, x**2 + y**2)
        return max_distance_sq