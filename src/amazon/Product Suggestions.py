# Description:
# Implement a function to return product suggestions using products from a product repository after each character is typed by the customer in the search bar.
# If there are more than THREE acceptable products, return the product name that is first in the alphabetical order.
# Only return product suggestions after the customer has entered two characters.
# Product suggestions must start with the characters already typed.
# Both the repository and the customer query should be compared in a CASE-INSENSITIVE way.
#
# Input:
# The input to the method/function consist of three arguments:
#
#     numProducts, an integer representing the number of various products in Amazon's product repository;
#     repository, a list of unique strings representing the various products in Amazon's product repository;
#     customerQuery, a string representing the full search query of the customer.
#
# Output:
# Return a list of a list of strings, where each list represents the product suggestions made by the system as the customer types each character of the customerQuery. Assume the customer types characters in order without deleting/removing any characters.
#
# Example:
# Input:
# numProducts = 5
# repository = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
# customerQuery = "mouse"
#
# Output:
# [["mobile", "moneypot", "monitor"],
# ["mouse", "mousepad"],
# ["mouse", "mousepad"],
# ["mouse", "mousepad"]]
#
# Explanation:
# The chain of words that will generate in the search box will be mo, mou, mous and mouse, and each
# line from output shows the suggestions of "mo", "mou", "mous" and "mouse", respectively in each line.
# For the suggestions that are generated for "mo", the matches that will be generated are:
# ["mobile", "mouse", "moneypot", "monitor", "mousepad"]. Alphabetically, they will be reordered to
# ["mobile", "moneypot", "monitor", "mouse", "mousepad"]. Thus, the suggestions are ["mobile", "moneypot", "monitor"]

class WordCount:
    def __init__(self, word, count):
        self.word = word
        self.count = count


class Trie:

    def __init__(self):
        self.child = {}
        self.word_list = []

    def insert_word(self, word_count: 'Word'):

        trie = self

        for char in word_count.word:
            if char not in trie.child:
                trie.child[char] = Trie()

            trie.child[char].word_list.append(word_count)
            trie = trie.child[char]

    def search(self, word):

        if len(word) < 2:
            return []

        trie = self
        for char in word:
            if char in trie.child:
                trie = trie.child[char]
            else:
                return []

        res = sorted(trie.word_list, key=lambda x: (-x.count, x.word))
        size = min(len(res), 3)

        return [res[i].word for i in range(size)]


import collections


def count_func(repository):
    res = []

    temp = collections.defaultdict(int)

    for word in repository:
        temp[word] += 1

    for word, count in temp.items():
        res.append(WordCount(word, count))

    return res


def product_suggestion(numProducts, repository, customerQuery):
    word_counts = count_func(repository)

    trie = Trie()
    for word_count in word_counts:
        trie.insert_word(word_count)

    res = []
    for i in range(2, len(customerQuery) + 1):
        res.append(trie.search(customerQuery[:i]))

    return res


print(product_suggestion(5, ["mobile", "mouse", "moneypot", "monitor", "mousepad"], 'mouse'))
