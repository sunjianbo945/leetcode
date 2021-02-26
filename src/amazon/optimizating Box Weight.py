from collections import Counter
from functools import lru_cache


# we may ask with same counts, what's the max weight we could get
def opt_weights(arr: list):
    counts = Counter(arr)
    half = sum(arr) / 2

    weights = list(set(arr))
    weights.sort(reverse=True)
    n = len(weights)

    res = []
    cands = []

    @lru_cache(None)
    def knapsack(idx, weight, count):
        if weight > half:
            cands.append((count, weight, res[:]))
            return weight, count
        if idx >= n:
            return weight, count

        # we use idx
        w = weights[idx]
        c = counts[w]
        nw = weight + w * c
        nc = count + c

        res.append(idx)
        nw, nc = knapsack(idx + 1, nw, nc)
        res.pop()

        # we don't use this idx
        weight1, count1 = knapsack(idx + 1, weight, count)

        # now compute return result
        if nw > half and weight1 > half:  # if both ways exceed 1/2 of total weight
            if nc < count1:
                return nw, nc
            elif nc == count1:
                if nw >= weight1:
                    return nw, nc
                else:
                    return weight1, count1
            else:
                return weight1, count1
        elif nw > half:  # if only the first way exceeds
            return nw, nc
        elif weight1 > half:  # if only the 2nd way exceeds
            return weight1, count1
        else:  # if none of them exeeds, lean on weight so we could reach 1/2 as fast as we could
            if nw >= weight1:
                return nw, nc
            else:
                return weight1, count1

    wf, cf = knapsack(0, 0, 0)
    print(f'count={cf}, weight={wf}')
    print(cands)

    res = None
    minc, maxw = float('inf'), float('-inf')
    for c, w, i in cands:
        if c < minc:
            minc, maxw, res = c, w, i
        elif c == minc:
            if w > maxw:
                minc, maxw, res = c, w, i

    ret = []
    for i in res:
        ret.extend([weights[i]] * counts[weights[i]])
    # print(f'sol={ret}')
    return ret


print(opt_weights([2, 1, 1, 1]))  # [1, 1, 1]
print(opt_weights([1, 1, 1, 1]))  # [1, 1, 1, 1]
print(opt_weights([15, 20, 20, 20, 50]))  # [50, 15]
print(opt_weights([9, 20, 20, 20, 50]))  # [20, 20, 20]
print(opt_weights([4, 5, 4, 1]))  # [4, 4]
print(opt_weights([1, 2, 3, 4, 5]))  # [5, 4]
print(opt_weights([20, 10, 1, 1]))  # [20]
print(opt_weights([1, 2, 2, 3, 3, 10]))  # [20]
print(opt_weights([10, 2, 2, 3, 3, 1]))  # [20]

# print(optimizeBox([20, 15, 20, 50, 20]))
# # -> [50, 15]
# print(optimizeBox([10, 4, 4, 4, 3]))
# # -> [10, 3]
# print(optimizeBox([5, 3, 2, 4, 1, 2]))
# # -> [5,4]
# print(optimizeBox([20, 15, 20, 50, 20]))
# # ->[50,15]
# print(optimizeBox([10, 9, 9, 6, 5, 4, 3, 2, 1]))
# # ->[10,9,9]
#
# print(optimizeBox([2, 1, 1, 1]))
# # ->The result should be [1,1,1] but I am getting [2]

def opt_weights2(arr: list):
    num_count = Counter(arr)
    nums = sorted(num_count.keys(), reverse=True)
    n = len(nums)
    target = sum(arr) / 2
    ans = [[0] * (len(arr) + 1), 0]

    def dfs(pos, weight, cur):
        nonlocal ans
        if weight > target and len(cur) <= len(ans[0]):
            if len(cur) < len(ans[0]) or weight > ans[1]:
                ans[0] = cur
                ans[1] = weight
            return
        if pos >= n: return

        for i in range(pos, len(nums)):
            num = nums[i]
            count = num_count[num]
            dfs(i + 1, weight + num * count, cur + [num] * count)

    dfs(0, 0, [])
    return ans[0]


print(opt_weights2([2, 1, 1, 1]))  # [1, 1, 1]
print(opt_weights2([1, 1, 1, 1]))  # [1, 1, 1, 1]
print(opt_weights2([15, 20, 20, 20, 50]))  # [50, 15]
print(opt_weights2([9, 20, 20, 20, 50]))  # [20, 20, 20]
print(opt_weights2([4, 5, 4, 1]))  # [4, 4]
print(opt_weights2([1, 2, 3, 4, 5]))  # [5, 4]
print(opt_weights2([20, 10, 1, 1]))  # [20]
print(opt_weights2([1, 2, 2, 3, 3, 10]))  # [20]
