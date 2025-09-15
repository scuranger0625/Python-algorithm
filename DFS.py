def dfs(u, neigh, seen):
    if u in seen: return
    seen.add(u)
    # 在這裡處理 u
    for v in neigh(u):
        dfs(v, neigh, seen)
