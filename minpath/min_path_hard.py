import collections
def min_path_medium(path):
    # directions = [(1,0),(0,1),(-1,0),(-1,0)]
    # m,n = len(path),len(path[0])

    # def dfs(i, j, v):
    #     seen.add((i, j))
    #     dp[i][j] = min(dp[i][j], v)
    #     for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
    #         if 0 <= x < m and 0 <= y < n and path[x][y] != float("inf") and (x, y) not in seen:
    #             dfs(x, y, v + path[x][y])
    #     seen.discard((i, j))

    # def bfs(i,j,v):
    #     q = collections.deque()
    #     q.append((i,j,v))
    #     minAtTHisPlace = float("inf")
    #     count = 0

    #     while q:
    #         x,y,val = q.popleft()
    #         count += val
    #         for d1,d2 in directions:
    #             di = x + d1
    #             dj = y + d2

    #             if 0<=di<m and 0<=dj<n and path[di][dj] < val and (di,dj) not in seen:
    #                 q.append((di,dj,path[di][dj]))
    #                 # dp[di][dj] = min(dp[di][dj],val)
    #     dp[i][j] = min(dp[i][j],minAtThisPlace)

    # seen = set()
    # m, n = len(path), len(path[0])
    # dp = [[float("inf")] * n for _ in range(m)]
    # for i in range(m):
    #     for j in range(n):
    #         if (i,j) not in seen:
    #         # if path[i][j] != float("inf"):
    #             dp[i][j] = bfs(i, j, path[i][j])
    #             seen.add((i,j))
    # return min(c for row in dp for c in row)

	def BFS(r, c):
		nonlocal best, best_path, R, C, path

		if path[r][c] < best:
			best = path[r][c]
			best_path = set([(r,c)])
		
		#(t) total gold, (r) row, (c) column, (p) path
		q = [(path[r][c], r, c, set([(r,c)]))]

		while q:
			next_level = []
			for t, r, c, p in q:
				for i, j in ((r+1,c), (r-1,c), (r,c+1), (r,c-1)):
					if 0 <= i < R and 0 <= j < C and path[i][j]:
						if (i,j) not in p:
							next_level.append((t+path[i][j], i, j, p|set([(i,j)])))
							if t + path[i][j] < best:
								best = t + path[i][j]
								best_path = p|set([(i,j)])
			q = next_level

	R, C = len(path), len(path[0])
	best = float("inf")
	best_path = set()

	for r in range(R):
		for c in range(C):
			if path[r][c]:
				if (r,c) not in best_path:
					BFS(r,c)

	return best

    # m, n, q, goldCellId, ans = len(path), len(path[0]), [], 0, float("inf")
    # oneCellTrace = [[0] * n for _ in range(m)]
    # for i in range(m):
    #     for j in range(n):
    #         if path[i][j]:
    #             oneCellTrace[i][j] = 1 << goldCellId
    #             goldCellId += 1
    #             q.append((i, j, path[i][j], oneCellTrace[i][j]))
    # for i, j, sum, trace in q:
    #     ans = min(sum, ans)
    #     for r, c in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
    #         if r >= 0 and r < m and c >= 0 and c < n and path[r][c] < path[i][j] and not (trace & oneCellTrace[r][c]):
    #             q.append((r, c, path[r][c] + sum, trace | oneCellTrace[r][c]))
    # return ans

grid = []
f = open("./min_path_hard_input.txt","r")
for line in f:
        grid.append([int(x) for x in line.split(' ')])
f.close()


f = open("./min_path_hard_output.txt", "w")
f.write(str(min_path_medium(grid)))
f.close()