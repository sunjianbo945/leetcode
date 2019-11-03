# [6,2,4,9] -> find the min interval [[2,4],[4,6]]


def main(a):

    sa= sorted(a)
    min_num = float('inf')
    res = []
    for i in range(1,len(sa)):

        if sa[i]-sa[i-1]< min_num:
            min_num = sa[i]-sa[i-1]
            res.clear()
            res.append([sa[i-1],sa[i]])
        elif sa[i]-sa[i-1]== min_num:
            res.append([sa[i-1],sa[i]])

    return res