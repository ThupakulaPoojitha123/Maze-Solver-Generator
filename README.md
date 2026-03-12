# Maze Solver & Generator

## Description
Generates random mazes using DFS and solves them using BFS pathfinding.

## Features
- Random maze generation
- BFS-based pathfinding
- Visual maze display
- Configurable maze size

## Usage
```python
maze = Maze(rows=11, cols=11)
maze.generate()
path = maze.solve_bfs((0, 0), (10, 10))
maze.display(path)
```

## Run
```bash
python maze.py
```
