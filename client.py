class HarrisNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.marked = False

class HarrisList:
    """
    Harris Lock-Free Ordered Linked List.
    Separates deletion into logical tag marking and physical node unlinking.
    """
    def __init__(self):
        self.head = HarrisNode(-float("inf"))
        self.tail = HarrisNode(float("inf"))
        self.head.next = self.tail

    def insert(self, key, value):
        curr = self.head
        while curr.next and curr.next.key < key:
            curr = curr.next
        if curr.next and curr.next.key == key:
            if not curr.next.marked:
                curr.next.value = value
                return False
        node = HarrisNode(key, value)
        node.next = curr.next
        curr.next = node
        return True

    def delete(self, key):
        curr = self.head
        while curr.next and curr.next.key < key:
            curr = curr.next
        target = curr.next
        if target and target.key == key and not target.marked:
            target.marked = True
            curr.next = target.next
            return True
        return False

    def find(self, key):
        curr = self.head.next
        while curr and curr.key < key:
            curr = curr.next
        if curr and curr.key == key and not curr.marked:
            return curr.value
        return None
