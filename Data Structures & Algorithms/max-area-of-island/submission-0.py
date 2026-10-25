class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))

        rows, cols = len(grid), len(grid[0])
        visited: set = set()
        area = 0

        def bfs(r, c):
            queue = collections.deque([(r, c)])
            visited.add((r, c))
            queue.append((r, c))
            temp_area = 1

            while queue:
                row, col = queue.popleft()

                for dr, dc in DIRECTIONS:
                    nr, nc = row + dr, col + dc
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == 1
                        and (nr, nc) not in visited
                    ):
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                        temp_area += 1
            return temp_area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = max(area, bfs(r, c))
        return area