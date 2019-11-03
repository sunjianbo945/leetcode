# [2,1,3,8,6] -> find the maximum number that can be sort individually, then will resolve the sorted array


def main(a):
    res = []
    min_num = float('inf')
    for i in range(len(a)-1,-1,-1):
        if a[i] < min_num:
            min_num = a[i]

        res=[min_num] + res

    ans = 1

    for i in range(1,len(res)):
        if res[i]!=res[i-1]:
            ans+=1

    return ans
