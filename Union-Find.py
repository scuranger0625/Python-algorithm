parent = list(range(n))
size = [1] * n

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb: return False
    if size[ra] < size[rb]: ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]
    return True
