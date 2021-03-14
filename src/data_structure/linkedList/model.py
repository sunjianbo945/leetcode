class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class NodeWithRadom:
    def __init__(self, x: int, next: 'NodeWithRadom' = None, random: 'NodeWithRadom' = None):
        self.val = int(x)
        self.next = next
        self.random = random