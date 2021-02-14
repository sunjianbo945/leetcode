def main(arr):
    target = 'Y' * len(arr[0])
    count, res = 0, 0
    for calendar in arr:
        if calendar == target:
            count += 1
        else:
            res = max(res, count)
            count = 0

    return max(res, count)
