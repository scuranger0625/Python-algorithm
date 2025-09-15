from collections import deque

def bfs(start, neigh):
    q = deque([start])
    seen = {start}
    while q:
        u = q.popleft()
        # 在這裡處理 u
        for v in neigh(u):
            if v not in seen:
                seen.add(v)
                q.append(v)
