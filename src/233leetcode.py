def countDigitOne(self, n: int) -> int:
    # trivial solution O(n^2), loop each int, count 1's
    res = 0
    k = 1
    while k <= n:
        # there are 2 patterns, one is ending 1's, like 1, 11, 21, 31, ...
        # the other is from 10-19, 100-199, 1000-1999, leading 1's.
        #
        # In order to include them in full, we need digit >= 2, this
        # is equivalent to (digit + 8) // 10 >= 1. If not digit 2, then we could
        # have 0 or 1. For 0, there is no change to the counts. For 1, we need
        # to count for r. For example, for 16, we need to count 10-16, not to the
        # full 10-19.

        # Then we break these 2 parts to each digit in the number.
        q, r = divmod(n, k)  # for kth digit from right
        full = (q + 8) // 10 * k
        partial = r + 1 if q % 10 == 1 else 0  # 0 because they are count as full above
        res += full + partial
        k *= 10

    return res

    # Examples:
    # 121     k=1                               k=2                              k=3
    # full    12 (11, 21, ... 121) (ending 1's) 20 (10-19, 110-119) (middle 1's) 0
    # partial 1  (1)                            0                                22 (100-121)
    # total 55
    #
    # 122     k=1                                  k=2                              k=3
    # full    13 (1, 11, 21, ... 121) (ending 1's) 20 (10-19, 110-119) (middle 1's) 0
    # partial 0                                    0                                23 (100-122)
    # total 56
    #
    # 111     k=1                                  k=2                      k=3
    # full    11 (11, 21, ... 121) (ending 1's)    10 (10-19) (leading 1's) 0
    # partial 1 (1)                                2 (110-111)              12 (100-111)
    # total 36
    #
    # 234     k=1                                  k=2