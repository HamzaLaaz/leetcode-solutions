from collections import deque

def findSafeWalk(grid: list[list[int]], health: int) -> bool:
    if grid[0][0] and health <= 0:
        return False
    if grid[0][0] and health > 0:
        health -= 1
    l_r = len(grid)
    l_c = len(grid[0])
    queue = deque([(0, 0, health)])
    d = {(-1, 0), (0, 1), (1, 0), (0, -1)}
    visited = {(0, 0, health)}
    while queue:
        r, c, hp = queue.popleft()
        if r == l_r - 1 and c == l_c - 1:
            return True
        for x, y in d:
            nr, nc = r + x, c + y
            if 0 <= nr < l_r and 0 <= nc < l_c:
                new_hp = hp - grid[nr][nc]
                if new_hp <= 0:
                    continue
                point = (nr, nc, new_hp)
                if point not in visited:
                    visited.add(point)
                    queue.append(point)
    return False
