# write an algorithm to help amazon identify the top N competitors mentioned online
from typing import *
import collections
import heapq


def count_fun(reviews, competitors):
    competitors_set = set(competitors)
    res = collections.defaultdict(int)
    for review in reviews:
        words = review.split(' ')
        for word in words:
            if word in competitors_set:
                res[word]+=1

    return res


def find(numCompetitors:int, topNcompetitors:int,competitors:List[int],numReviews:int, reviews:List[str]) -> List[str]:
    '''
    numCompetitors : an iteger representing the number of competitors for the Echo device
    topNcompetitors : an integer representing the number of top competitors evaluated from the list of competitors that are a good competition to Amazon
    competitors: : a list of string representing the competitors
    numReviews: an integer representing the number of reviews from different websites that are identified by the automated webcrawler
    reviews: a list of string where each element is string that consists of space spearated words representing user reviews
    '''
    res = []
    if numReviews == 0 or numCompetitors == 0: return res

    competitors_count = count_fun(reviews, competitors)

    heap = []

    for competitor, count in competitors_count.items():
        heapq.heappush(heap, (-count,competitor))

    topNcompetitors = topNcompetitors if topNcompetitors<numCompetitors else numCompetitors

    for i in range(topNcompetitors):
        _, competitor = heapq.heappop(heap)
        res.append(competitor)

    return res


print(find(6,2,['newshop','shopnow','afshion','fashionbeats','mymarket','tcellular' ], 6,
          ['newshop is providing good services in the city',
           'everyone should use newshop',
           'best services by newshop',
           'fashionbeats has great services in the city',
           'I am proud to have fashionbeats',
           'mymarket has awesome services',
           'Thanks Newshop for the quick delivery']))


