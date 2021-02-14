# find the min number that can be divide by 7

def main(a):
    res = float('inf')
    for i in range(len(a)):
        if a[i] < res and a[i] % 7 == 0:
            res = a[i]

    return res


