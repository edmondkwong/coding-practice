import sys

themap = []
visited = []


def dfs(r, c, start, end, themap, visited):
    if r < 0 or r >= len(visited) or c < 0 or c >= len(visited[0]) or themap[r][c] == '-' or visited[r][c] is True:
        return
    elif themap[r][c] == '*':
        visited[r][c] = True
        if r < start['r']:
            start['r'] = r
        if c < start['c']:
            start['c'] = c
        if r > end['r']:
            end['r'] = r
        if c > end['c']:
            end['c'] = c
        dfs(r - 1, c, start, end, themap, visited)
        dfs(r + 1, c, start, end, themap, visited)
        dfs(r, c - 1, start, end, themap, visited)
        dfs(r, c + 1, start, end, themap, visited)


for line in sys.stdin:
    if line == '\n':
        break
    row = []
    visitedRow = []
    for c in line[:-1]:
        row.append(c)
        visitedRow.append(False)
    themap.append(row)
    visited.append(visitedRow)

result = []
for row in range(len(themap)):
    for col in range(len(themap[0])):
        if themap[row][col] == '*' and visited[row][col] is False:
            start = {'r': row, 'c': col}
            end = {'r': row, 'c': col}
            dfs(row, col, start, end, themap, visited)
            result.append((start['r']+1, start['c']+1))
            result.append((end['r']+1, end['c']+1))

for i in result:
    print(i)
