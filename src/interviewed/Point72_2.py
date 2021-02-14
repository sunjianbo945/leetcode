import bisect


def main(price_transaction):  # [[100,100], [200, 300],...]
    price_transaction.sort(key=lambda x: x[0])
    transactions = [price_transaction[0][1]]
    for i in range(1, len(price_transaction)):
        transactions.append(transactions[-1] + price_transaction[i][1])
    target = transactions[-1] * 0.8
    idx = bisect.bisect_left(transactions, target)
    return price_transaction[idx][0]
