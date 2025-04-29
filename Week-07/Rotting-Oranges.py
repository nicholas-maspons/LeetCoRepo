# 994. Rotting Oranges

from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0  

        minutes = -1  
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            minutes += 1
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:  # W names
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))

        return minutes if fresh == 0 else -1
