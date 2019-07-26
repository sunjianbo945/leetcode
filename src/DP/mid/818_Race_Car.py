class Solution:
    def racecar(self, target: int) -> int:
        from queue import Queue
        res = 0
        q = Queue()
        q.put((0, 1))
        s = set()
        s.add((0, 1))
        while not q.empty():
            size = q.qsize()
            for i in range(size):
                position, speed = q.get()
                if position == target:
                    return res
                np, ns = position + speed, speed * 2
                if (np, ns) not in s and np > 0 and np < target * 2:
                    s.add((np, ns))
                    q.put(((np, ns)))

                np, ns = position, 1 if speed < 0 else -1
                if (np, ns) not in s and np > 0 and np < target * 2:
                    s.add((np, ns))
                    q.put(((np, ns)))
            res += 1
        return -1


def main():
    print(Solution().racecar(5))


if __name__=='__main__':
    main()