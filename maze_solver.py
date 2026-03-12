import random
from collections import deque

class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[1] * cols for _ in range(rows)]
    
    def generate(self):
        stack = [(0, 0)]
        self.grid[0][0] = 0
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        
        while stack:
            x, y = stack[-1]
            random.shuffle(directions)
            found = False
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.rows and 0 <= ny < self.cols and self.grid[nx][ny] == 1:
                    self.grid[nx][ny] = 0
                    self.grid[x + dx // 2][y + dy // 2] = 0
                    stack.append((nx, ny))
                    found = True
                    break
            
            if not found:
                stack.pop()
        
        self.grid[self.rows - 1][self.cols - 1] = 0
    
    def solve(self, start=(0, 0), end=None):
        if end is None:
            end = (self.rows - 1, self.cols - 1)
        
        queue = deque([start])
        visited = {start}
        parent = {start: None}
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            x, y = queue.popleft()
            if (x, y) == end:
                path = []
                while (x, y) is not None:
                    path.append((x, y))
                    x, y = parent[(x, y)] if parent[(x, y)] else (None, None)
                return path[::-1]
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.rows and 0 <= ny < self.cols and self.grid[nx][ny] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    parent[(nx, ny)] = (x, y)
                    queue.append((nx, ny))
        
        return []
    
    def display(self, path=None):
        path_set = set(path) if path else set()
        for i in range(self.rows):
            for j in range(self.cols):
                if (i, j) in path_set:
                    print("* ", end="")
                elif self.grid[i][j] == 0:
                    print("  ", end="")
                else:
                    print("█ ", end="")
            print()

if __name__ == "__main__":
    print("\n=== MAZE GENERATOR & SOLVER ===")
    rows = int(input("Enter maze rows (odd number, e.g., 11): "))
    cols = int(input("Enter maze columns (odd number, e.g., 11): "))
    
    maze = Maze(rows, cols)
    print("\nGenerating maze...")
    maze.generate()
    
    print("\nGenerated Maze:")
    maze.display()
    
    solve = input("\nSolve the maze? (yes/no): ").lower()
    if solve == 'yes':
        print("\nSolving maze...")
        path = maze.solve()
        if path:
            print("\nSolved Maze (path marked with *)")
            maze.display(path)
            print(f"\nPath length: {len(path)} steps")
        else:
            print("No solution found!")