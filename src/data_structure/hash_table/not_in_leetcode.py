# The people who buy ads on our network don't have enough data about how ads are working for
# their business. They've asked us to find out which ads produce the most purchases on their website.
#
# Our client provided us with a list of user IDs of customers who bought something on a landing page
# after clicking one of their ads:
#
# # Each user completed 1 purchase.
# completed_purchase_user_ids = [
#    "3123122444","234111110", "8321125440", "99911063"]
#
# And our ops team provided us with some raw log data from our ad server showing every time a
# user clicked on one of our ads:
# ad_clicks = [
#   #"IP_Address,Time,Ad_Text",
#   "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
#   "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
#   "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
#   "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
#   "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
#   "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
# ]
#
# The client also sent over the IP addresses of all their users.
#
# all_user_ips = [
#   #"User_ID,IP_Address",
#    "2339985511,122.121.0.155",
#   "234111110,122.121.0.1",
#   "3123122444,92.130.6.145",
#   "39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
#   "8321125440,82.1.106.8",
#   "99911063,92.130.6.144"
# ]
#
# Write a function to parse this data, determine how many times each ad was clicked,
# then return the ad text, that ad's number of clicks, and how many of those ad clicks
# were from users who made a purchase.
#
# Expected output:
# Bought Clicked Ad Text
# 1 of 2  2017 Pet Mittens
# 0 of 1  The Best Hollywood Coats
# 3 of 3  Buy wool coats for your pets
from collections import Counter
from math import inf


def adsConversionRate(completed_purchase_user_ids, ad_clicks, all_user_ips):
    user_bought = set(completed_purchase_user_ids)
    ad_name = {}
    for each in ad_clicks:
        ad_ip, _, name = each.split(',')
        ad_name[ad_ip] = name

    ad_clicked_count = Counter()
    ad_bought_count = Counter()
    for each in all_user_ips:
        user, ip = each.split(',')
        if ip not in ad_name: continue
        ad_clicked_count[ad_name[ip]] += 1
        ad_bought_count[ad_name[ip]] += 1 if user in user_bought else 0

    for each, count in ad_clicked_count.items():
        print(f'{ad_bought_count[each]} of {count} {each}')


if __name__ == '__main__':
    # "User_ID,IP_Address",
    all_user_ips = [
        "2339985511,122.121.0.155",
        "234111110,122.121.0.1",
        "3123122444,92.130.6.145",
        "39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
        "8321125440,82.1.106.8",
        "99911063,92.130.6.144"]

    ad_clicks = [
        # "IP_Address,Time,Ad_Text",
        "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
        "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
        "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
        "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
        "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
        "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
    ]

    completed_purchase_user_ids = [
        "3123122444", "234111110", "8321125440", "99911063"]

    adsConversionRate(completed_purchase_user_ids, ad_clicks, all_user_ips)
# ----------------------------------------------------------------------------------------------------------------------
"""
Hudson River Trading, LLC

Implement a hash table (HashMap) with the following functions in O(1):
- insert(key, value)
- delete(key)
- get(key)
- get_random_key()

The hash table must match the behavior tested in the test suite, which matches the
behavior of a regular python dictionary.

You may use any built-in Python functions and data structures. Keep in mind that all
operations must be in O(1). For example, you are not allowed to use the dict.keys()
function, or "key in list".

Assume that there will be no collisions in any of the inserts per hash table instance.
"""

import unittest
import random
from collections import defaultdict


class Map:

    def __init__(self):
        self.key_loc = {}
        self.key_val = {}
        self.keys = []

    def __getitem__(self, key):
        return self.key_val[key]

    def __setitem__(self, key, val):
        if key not in self.key_loc:
            self.key_loc[key] = len(self.keys)
            self.keys.append(key)

        self.key_val[key] = val

    def __delitem__(self, key):
        # O(1)
        del self.key_val[key]

        last_key = self.keys[-1]
        curr_loc = self.key_loc[key]

        self.key_loc[last_key] = curr_loc
        self.keys[curr_loc] = last_key

        self.keys.pop()
        del self.key_loc[key]

    def __str__(self):
        # Implement this if you'd like to print your hash table.
        pass

    def __len__(self):
        return len(self.keys)

    def get_random_key(self):
        # O(n)
        return random.choice(self.keys)


# no need to modify anything below

class BasicHashMapTest(unittest.TestCase):

    def setUp(self):
        self.map = Map()

    def test_insert(self):
        self.map[0] = "Hudson River Trading"
        self.map[1] = "New York"

    def test_insert_get(self):
        self.map[0] = "Hudson River Trading"
        self.map[1] = "New York"

        self.assertEqual(self.map[0], "Hudson River Trading")
        self.assertEqual(self.map[1], "New York")

    def test_insert_get_delete(self):
        self.map[0] = "Hudson River Trading"
        self.map[1] = "New York"

        self.assertEqual(self.map[0], "Hudson River Trading")
        self.assertEqual(self.map[1], "New York")

        del self.map[1]

        # assert keys exist
        self.assertEqual(self.map[0], "Hudson River Trading")

        # assert delete key does not exist
        with self.assertRaises(KeyError):
            self.map[1]

    def test_full_basic(self):
        self.map[0] = "Hudson River Trading"
        self.map[1] = "New York"

        self.assertEqual(len(self.map), 2)
        self.assertEqual(self.map[0], "Hudson River Trading")
        self.assertEqual(self.map[1], "New York")

        del self.map[1]

        self.assertEqual(len(self.map), 1)
        # assert keys exist
        self.assertEqual(self.map[0], "Hudson River Trading")
        # assert delete key does not exist
        with self.assertRaises(KeyError):
            self.map[1]

        self.map[2] = "Value 1"

        self.assertEqual(len(self.map), 2)

        del self.map[2]
        self.map[3] = "Value 2"

        self.assertEqual(len(self.map), 2)
        self.assertEqual(self.map[3], "Value 2")
        with self.assertRaises(KeyError):
            self.map[2]


class RandomKeyHashMapTest(unittest.TestCase):

    def setUp(self):
        self.map = Map()

    def verify_random_keys(self, possible_keys):
        rands = defaultdict(int)
        for _ in range(1000000):
            rands[self.map.get_random_key()] += 1

        try:
            self.assertEqual(set(rands.keys()), set(possible_keys))
        except AssertionError:
            print("Your random function generated non-existing keys.")
            raise

        total = sum(rands.values())
        expected_probability = round(1 / float(len(possible_keys)), 2)
        for k, v in rands.items():
            probability = round(v / float(total), 2)
            try:
                self.assertEqual(probability, expected_probability)
            except AssertionError:
                print(
                    f"{k}'s probablity is {probability}. "
                    f"Expected: {expected_probability}."
                )
                raise

    def test_two_keys(self):
        self.map[0] = "Hudson River Trading"
        self.map[1] = "New York"
        self.verify_random_keys([0, 1])

    def test_four_keys(self):
        self.map[0] = "Hudson River Trading"
        self.map[1] = "Hudson River Trading"
        self.map[2] = "LLC"
        self.map[3] = "New York"
        self.map[4] = "NY"
        self.map[5] = "NY"
        del self.map[0]
        del self.map[5]
        self.verify_random_keys([1, 2, 3, 4])


# 第一题，给一个array，比如(5,3,6,1,3)和一个数字K，然后问移除连续个数字K之后能达到最小的数组的amplitude（数组最大值-最小值）是多少。
# 比如上面的数组，如果K=2，则移除6,1之后即可得到(5,3,3)，amplitude是2。
# 最优解法是O(n)。
class SolutionMinAplitude:
    def minAplitude(self, arr, k):
        n = len(arr)
        forward_max, forward_min, backward_max, backward_min = [-inf], [inf], [-inf], [inf]
        for i in arr:
            forward_max.append(max(i, forward_max[-1]))
            forward_min.append(min(i, forward_min[-1]))

        for i in arr[::-1]:
            backward_max.append(max(i, backward_max[-1]))
            backward_min.append(min(i, backward_min[-1]))

        backward_min = backward_min[::-1]
        backward_max = backward_max[::-1]

        res = inf
        for i in range(n - k):
            range_max = max(forward_max[i], backward_max[i + k])
            range_min = min(forward_min[i], backward_min[i + k])

            res = min(res, range_max - range_min)

        return res


# 第四题是给一个NxM的棋盘，每个格子有不同的权重，放两个rook（象棋的車）上去，怎样让两个rook站的位置获得最大的权重，条件限制是他们不能互相吃掉。
# 也不难，O(MN)复杂度算出来。
class SolutionTwoRook:
    def maxTwoWeight(self, board):
        m, n = len(board), len(board[0])
        tl = [[-inf] * n for _ in range(m)]
        tr = [[-inf] * n for _ in range(m)]
        bl = [[-inf] * n for _ in range(m)]
        br = [[-inf] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    tl[i][j] = board[i][j]
                elif i == 0:
                    tl[i][j] = max(board[i][j], tl[i][j - 1])
                elif j == 0:
                    tl[i][j] = max(board[i][j], tl[i - 1][j])
                else:
                    tl[i][j] = max(board[i][j], tl[i][j - 1], tl[i - 1][j])

        for i in range(m - 1, -1, -1):
            for j in range(n):
                if i == m - 1 and j == 0:
                    bl[i][j] = board[i][j]
                elif i == m - 1:
                    bl[i][j] = max(board[i][j], bl[i][j - 1])
                elif j == 0:
                    bl[i][j] = max(board[i][j], bl[i + 1][j])
                else:
                    bl[i][j] = max(board[i][j], bl[i][j - 1], bl[i + 1][j])

        for i in range(m):
            for j in range(n - 1, -1, -1):
                if i == 0 and j == n - 1:
                    tr[i][j] = board[i][j]
                elif i == 0:
                    tr[i][j] = max(board[i][j], tr[i][j + 1])
                elif j == n - 1:
                    tr[i][j] = max(board[i][j], tr[i - 1][j])
                else:
                    tr[i][j] = max(board[i][j], tr[i][j + 1], tr[i - 1][j])

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    br[i][j] = board[i][j]
                elif i == m - 1:
                    br[i][j] = max(board[i][j], br[i][j + 1])
                elif j == n - 1:
                    br[i][j] = max(board[i][j], br[i + 1][j])
                else:
                    br[i][j] = max(board[i][j], br[i][j + 1], br[i + 1][j])
        res = 0
        for i in range(m):
            for j in range(n):
                curr = board[i][j]
                tlMax = tl[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0
                trMax = tr[i - 1][j + 1] if i - 1 >= 0 and j + 1 < n else 0
                blMax = bl[i + 1][j - 1] if i + 1 < m and j - 1 >= 0 else 0
                brMax = br[i + 1][j + 1] if i + 1 < m and j + 1 < n else 0

                res = max(res, curr + max(tlMax, trMax, blMax, brMax))

        return res

if __name__ == "__main__":
    # section 1
    # print("\n==== Running basic tests ====\n")
    # basic_suite = unittest.TestSuite()
    # basic_suite.addTest(unittest.makeSuite(BasicHashMapTest))
    # basic_test = unittest.TextTestRunner(verbosity=2).run(basic_suite)
    #
    # if basic_test.errors or basic_test.failures:
    #     # If above basic test fails, do not run next random test.
    #     sys.exit(1)
    #
    # print("\n==== Running random keys tests ====\n")
    # random_suite = unittest.TestSuite()
    # random_suite.addTest(unittest.makeSuite(RandomKeyHashMapTest))
    # random_test = unittest.TextTestRunner(verbosity=2).run(random_suite)

    # section 2
    # print(SolutionMinAplitude().minAplitude([3, 5, 6, 1, 3], 3))

    # section 3
    print(SolutionTwoRook().maxTwoWeight([[1,3],[4,2]]))