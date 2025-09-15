1. BFS

口訣：Queue + Seen → pop → push 鄰居

q=deque([s]); seen={s}
while q:
    u=q.popleft()
    for v in neigh(u):
        if v not in seen: seen.add(v); q.append(v)

2. DFS

口訣：遞迴 → 標記 → 探鄰居

def dfs(u):
    if u in seen: return
    seen.add(u)
    for v in neigh(u): dfs(v)

3. Union-Find

口訣：find 路壓 → union 按大

def find(x):
    while p[x]!=x: p[x]=p[p[x]]; x=p[x]
    return x
def union(a,b):
    ra,rb=find(a),find(b)
    if ra!=rb: p[rb]=ra

4. Sliding Window

口訣：右指標加 → 左指標縮

l=0
for r,ch in enumerate(s):
    while condition不滿足: l+=1

5. Binary Search

口訣：lo < hi → mid → 收縮區間

lo,hi=0,len(nums)
while lo<hi:
    mid=(lo+hi)//2
    if nums[mid]<target: lo=mid+1
    else: hi=mid

6. Two Pointers

口訣：快慢指標 → 遇到條件就搬

i=0
for j in range(len(nums)):
    if valid(nums[j]): nums[i]=nums[j]; i+=1

7. Prefix Sum

口訣：累加 → 查區間差

pre=[0]
for x in nums: pre.append(pre[-1]+x)

8. DP (序列)

口訣：狀態轉移 → max(dp)

dp=[1]*n
for i in range(n):
    for j in range(i): if cond: dp[i]=max(dp[i],dp[j]+1)

🎯 怎麼「背」？（不用死記硬背）

只記口訣（比如 BFS = Queue+Seen+pop/push）。

每天 10 分鐘抄骨幹一次 → 記住「結構」就好。

遇到題目時先喊口訣，再把骨幹打出來。細節靠 debug。
