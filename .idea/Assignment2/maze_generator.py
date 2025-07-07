import random
import sys
sys.setrecursionlimit(10000)  # Increase recursion limit for large mazes

def create_empty_maze(rows, cols):
    # Initialize maze with all walls (1s)
    maze = [[1 for _ in range(cols)] for _ in range(rows)]
    return maze

def print_maze(maze):
    for row in maze:
        print(' '.join(str(cell) for cell in row))
    print()

def generate_maze_dfs(maze, x, y):
    # Mark current cell as path (0)
    maze[x][y] = 0

    # Randomly order directions: up, down, left, right
    directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
    random.shuffle(directions)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        # Check if new cell is inside bounds and is still a wall
        if 1 <= nx < len(maze) - 1 and 1 <= ny < len(maze[0]) - 1 and maze[nx][ny] == 1:
            # Break wall between current and next cell
            maze[x + dx // 2][y + dy // 2] = 0
            generate_maze_dfs(maze, nx, ny)

def solve_maze_dfs(maze, x, y, end_x, end_y, path):
    if x == end_x and y == end_y:
        path.append((x, y))
        return True

    if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]) or maze[x][y] != 0:
        return False

    # Mark as visited
    maze[x][y] = 2

    # Explore all directions
    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        if solve_maze_dfs(maze, x+dx, y+dy, end_x, end_y, path):
            path.append((x, y))
            return True

    return False

def mark_solution_path(maze, path):
    for x, y in path:
        maze[x][y] = '*'

def main():
    rows, cols = 21, 21  # Must be odd numbers for proper maze structure

    # Step 1: Generate Maze
    maze = create_empty_maze(rows, cols)
    generate_maze_dfs(maze, 1, 1)
    print("Generated Maze (1 = Wall, 0 = Path):")
    print_maze(maze)

    # Step 2: Solve Maze
    path = []
    start_x, start_y = 1, 1
    end_x, end_y = rows - 2, cols - 2

    # Temporarily make sure end cell is path (just in case)
    maze[end_x][end_y] = 0

    if solve_maze_dfs(maze, start_x, start_y, end_x, end_y, path):
        path.reverse()  # DFS records path in reverse
        mark_solution_path(maze, path)
        print("Solved Maze (Path marked with '*'):")
        print_maze(maze)
    else:
        print("No solution found!")

if __name__ == "__main__":
    main()