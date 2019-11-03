# each matrix got
# every element (x,y) ->
# s= 0
#
# for i in range(x+1):
#     for j in rang(y+1):
#         s+= befor[i][j]
#
# after[i][j] = s

# question give after
# reverse to before

def main(after):

    before = [[0]* len(after[0]) for _ in range(len(after)) ]

    for i in range(len(after)):
        before[i][0] = after[i][0]

    for i in range(len(after)):
        for j in range(1,len(after[0])):
            before[i][j] = after[i][j]- after[i][j-1]

    for i in range(len(after),0,-1):
        for j in range(len(after[0])):
            before[i][j] = before[i][j]-before[i-1][j]

    return before

