#! /usr/bin/env python


class LinkedList:
    class Node:
        def __init__(self, val=None):
            self.val = val
            self.next = None

        def __str__(self):
            return str(self.val)

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        return  '< ' + ', '.join([str(i) for i in self.traverser()]) + ' >'

    def __len__(self):
        count = 0
        runner = self.head
        while runner:
            runner = runner.next
            count = count + 1
        return count

    def traverser(self):
        runner = self.head
        while runner.next:
            yield runner.val
            runner = runner.next

    def printlist(self):
        for i in self.traverser():
            print(i, end=", ")

    def append(self, val):
        if self.head is None:
            self.head = self.Node(val)
            self.last = self.head
        else:
            last = self.last
            node = self.Node(val)
            last.next = node
            self.last = node

    def extend(self, iterable):
        for i in iterable:
            self.append(i)

    def count(self, key):
        counter = 0
        for i in self.traverser():
            if i == key:
                counter += 1
        return counter

    def reverse(self):
        alpha = self.head
        beta = alpha.next
        alpha.next = None
        while beta:
            gamma = beta.next
            beta.next = alpha
            alpha = beta
            beta = gamma
        self.head = alpha
