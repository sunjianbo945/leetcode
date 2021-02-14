import collections

def max_flow_dfs(requests, N):
    graph = collections.defaultdict(lambda: collections.defaultdict(list))
    for name, src, dst in requests:
        graph[src][dst].append(name)

    def dfs(node, path, min_flow):
        current_min_flow = min_flow
        max_path = []

        for next_node, peoplelist in graph[node].items():
            if next_node in path:
                next_min_flow = min(min_flow, len(peoplelist))
                if len(max_path) < next_min_flow:
                    max_path = peoplelist[:current_min_flow]
                    current_min_flow = next_min_flow
            else:
                next_max_path, next_min_flow = dfs(next_node, path | {next_node}, min(min_flow, len(peoplelist)))
                if len(next_max_path) + len(peoplelist[:next_min_flow]) > len(max_path):
                    max_path = peoplelist[:next_min_flow] + next_max_path
                    current_min_flow = next_min_flow


        return max_path, current_min_flow
    res = []
    for i in range(N):
        next_max, _ = dfs(i, {i}, float('inf'))
        res.append(next_max)

    return res

if __name__ == '__main__':
    requests= [["Alex", 1, 2 ],
["Ben", 2, 1 ],
["Chris", 1, 2 ],
["David", 2, 3 ],
["Ellen", 3, 1 ],
["Frank", 4, 5 ]]
    ret = max_flow_dfs(requests,len(requests))