class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1,0), (1,0), (0,1), (0,-1)] #x,y
        ROWS, COLS = len(grid), len(grid[0]) 
        islands = 0
        visited = set()
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            while q:
                row, col = q.popleft()
                visited.add((row,col))
                for rd, cd in directions:
                    nrow, ncol = row + rd, col + cd
                    # water or land: land
                    # if land is visited only add unvisited land
                    # if in bound
                    if (nrow >=0 and ncol >=0 and ncol < COLS and nrow < ROWS and (grid[nrow][ncol] == "1") 
                        and (nrow,ncol) not in visited):
                        q.append((nrow,ncol))
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands

