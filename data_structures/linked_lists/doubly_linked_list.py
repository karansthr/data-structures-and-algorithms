#! /usr/bin/env python


class LinkedList:
    class Node:
        def __init__(self, val=None):
            self.val = val
            self.next = None
            self.prev = None

        def __str__(self):
            return str(self.val)

    def __init__(self):
        self.first = None
        self.last = None

    def __str__(self):
        return '< '+', '.join([str(i) for i in self.traverse_forward()]) + ' >'

    def __len__(self):
        count = 0
        runner = self.first
        while runner:
            runner = runner.next
            count = count + 1
        return count

    def traverse_forward(self):
        runner = self.first
        while runner:
            yield runner.val
            runner = runner.next

    def traverse_reverse(self):
        runner = self.last
        while runner:
            yield runner.val
            runner = runner.prev

    def printlist(self):
        for i in self.traverse_forward():
            print(i, end=", ")

    def printlist_reverse(self):
        for i in self.traverse_reverse():
            print(i, end=", ")

    def insert(self, val):
        if self.first is None:
            self.first = self.Node(val)
            self.last = self.first
        else:
            last = self.last
            node = self.Node(val)
            last.next = node
            node.prev = last
            self.last = node

    def insert_beginning(self, val):
        temp = self.Node(val)
        self.first.prev = temp
        temp.next = self.first
        self.first = temp

    def insert_end(self, val):
        temp = self.Node(val)
        temp.prev = self.last
        self.last.next = temp
        self.last = temp

    def insert_after(self, nodeval, val):
        traverser = self.first
        flag = True
        while traverser.val != nodeval:
            traverser = traverser.next
        else:
            flag = False

        if flag:
            t_next = traverser.next
            temp = self.Node(val)
            traverser.next = temp
            temp.prev = traverser
            temp.next = t_next

    def insert_before(self, nodeval, val):
        previous = None
        traverser = self.first
        flag = True
        while traverser.val != nodeval:
            previous = traverser
            traverser = traverser.next
        else:
            flag = False
        if flag:
            temp = self.Node(val)
            previous.next = temp
            temp.next = traverser
            temp.prev = previous

    def extend(self, iterable):
        for i in iterable:
            self.append(i)

    def count(self, key):
        counter = 0
        for i in self.traverse_forward():
            if i == key:
                counter += 1
        return counter

    def reverse(self):
        self.first = alpha = self.last
        beta = alpha.prev
        alpha.prev = None
        alpha.next = beta
        while beta:
            gamma = beta.prev
            beta.next = gamma
            beta.prev = alpha
            alpha = beta
            beta = gamma
        self.last = alpha
