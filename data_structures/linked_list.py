class LinkedList:
    class Node:
        def __init__(self, val=None):
            self.val = val
            self.next = None

        def __str__(self):
            return str(self.val)

    def __init__(self):
        self.head = self.Node()

    def __len__(self):
        count = 0
        traverser = self.head
        while not traverser:
            traverser = traverser.next
            count = count + 1
        return count

    def printlist(self):
        traverser = self.head
        while traverser:
            print(traverser.val, end=", ")
            traverser = traverser.next

    def last(self):
        previous = traverser = self.head
        while traverser:
            previous = traverser
            traverser = traverser.next
        return previous

    def append(self, val):
        if not len(self):
            self.head = self.Node(val)
        else:
            _last = self.last()
            node = self.Node(val)
            _last.next = node

    def extend(self, iterable):
        pass

    def count(self, key):
        pass

    def clear(self):
        pass

    def reverse(self):
        pass

    def remove(self, key):
        pass

    def remove_all(self, key):
        pass

    def merge_sort(self):
        pass

    def quick_sort(self):
        pass

    def insertion_sort(self):
        pass

    def selection_sort(self):
        pass

    def get_head(self):
        pass

    def get_tail(self):
        pass
