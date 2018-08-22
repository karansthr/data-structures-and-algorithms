class Stack:
    def __init__(self, max=None):
        '''
        :param max: optional argument for size of stack
        :type max: int
        '''
        self.max = max
        self.top = -1
        self.stack = []

    def push(self, element):
        '''
        if stack has some max defined than it will raise stackoverflow
        exception is stack is full.

        :param element: any object
        :raise: Exception
        '''
        if self.max and self.top + 1 == self.max:
            raise Exception('Stack overflow!')
        self.top += 1
        self.stack.append(element)

    def pop(self):
        '''
        if stack is empty then this function will return stackunderflow
        because there is no element on the top to return
        '''
        if self.top == -1:
            raise Exception('Stack underflow!')
        self.top -= 1
        return self.stack[-1]

    def peek(self):
        '''
        return element at the top of the stack without removing it from
        the stack
        '''
        if self.top == -1:
            return None
        return self.stack[-1]

    def is_empty(self):
        '''
        check if stack is empty and return boolean True if so, else False
        '''
        return True if self.top == -1 else False

    def is_full(self):
        '''
        check if stack is full and return boolean True if so, else False
        '''
        return True if self.max and self.top + 1 == max else False

    @property
    def size(self):
        '''
        number of element in the queue
        '''
        return self.top + 1

    def __str__(self):
        return str(self.stack)
