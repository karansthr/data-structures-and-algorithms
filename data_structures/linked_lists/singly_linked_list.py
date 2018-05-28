#! /usr/bin/env python


class LinkedList:
    class Node:
        def __init__(self, val=None):
            self.val = val
            self.next = None

        def __str__(self):
            return str(self.val)

    def __init__(self):
        self.first = None
        self.last = None

    def __str__(self):
        return '< ' + ', '.join([str(i) for i in self.traverser()]) + ' >'

    def __len__(self):
        count = 0
        runner = self.first
        while runner:
            runner = runner.next
            count = count + 1
        return count

    def traverser(self):
        runner = self.first
        while runner:
            yield runner.val
            runner = runner.next

    def printlist(self):
        for i in self.traverser():
            print(i, end=", ")
        else:
            print()

    def insert(self, val):
        if self.first is None:
            self.first = self.Node(val)
            self.last = self.first
        else:
            last = self.last
            node = self.Node(val)
            last.next = node
            self.last = node

    def insert_after(self, nodeval, val):
        traverser = self.first
        flag = True
        while traverser.val != nodeval:
            traverser = traverser.next
        else:
            flag = False

        if flag:
            print("found")
            t_next = traverser.next
            temp = self.Node(val)
            traverser.next = temp
            temp.next = t_next

    def insert_before(self, nodeval, val):
        previous = None
        traverser = self.first
        flag = True
        print("out",traverser.val,nodeval)
        while traverser.val != nodeval:
            previous = traverser
            traverser = traverser.next
            print("out",traverser.val,nodeval)
        else:
            flag = False
        if flag:
            temp = self.Node(val)
            previous.next = temp
            temp.next = traverser

    def insert_beginning(self, val):
        temp = self.Node(val)
        temp.next = self.first
        self.first = temp

    def insert_end(self, val):
        temp = self.Node(val)
        self.last.next = temp
        self.last = temp

    def remove(self, val):
        dummy = self.Node(None)
        dummy.next = current = self.first
        prev = dummy
        while current:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
                current = current.next

    def extend(self, iterable):
        for i in iterable:
            self.insert(i)

    def count(self, key):
        counter = 0
        for i in self.traverser():
            if i == key:
                counter += 1
        return counter

    def reverse(self):
        alpha = self.first
        beta = alpha.next
        alpha.next = None
        while beta:
            gamma = beta.next
            beta.next = alpha
            alpha = beta
            beta = gamma
        self.first = alpha
