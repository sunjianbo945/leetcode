'''
Combination:

nums = [...]
ans=[]

func dfs(n,s,cur):
    if cur.size ==n:
        ans.append(cur)
        return

    for i = s to nums.size():
        cur.append(nums[i])
        dfs(n,i+1,cur)
        cur.pop()


for i =0 to nums.size():
    dfs(i,0,[])


Permutation:

nums=[...]
ans = []
used = [False]* nums.size()

func dfs(n,cur):
    if cur.size()==n:
        ans.append(cur)
        return

    for i =0 to nums.size():
        if used[i]:
            continue
        used[i] = True
        cur.append(nums[i])
        dfs(n,cur)
        cur.pop()
        used[i] = False

for i=0 to nums.size():
    dfs(i,0,[])
'''