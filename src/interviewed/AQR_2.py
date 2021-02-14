# slicing window, the max of value of the min value in the window [2,5,3,4,6,8] -> 4

def main(a, m):
    queue = [0]
    for i in range(1, m):

        while queue and a[i] < a[queue[-1]]:
            queue.pop()

        queue.append(i)

    res = a[queue[0]]

    for i in range(m, len(a)):

        while queue and queue[0] <= i - m:
            queue.pop(0)

        while queue and a[i] < a[queue[-1]]:
            queue.pop()

        queue.append(i)
        res = max(res, a[queue[0]])

    return res
