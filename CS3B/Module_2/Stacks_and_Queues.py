# Stack is LIFO
class Stack:
    def __init__(self):
        self._stack = list()

    def push(self, data):
        self._stack.append(data)

    def pop(self):
        if not self._stack:
            return None
        else:
            return self._stack.pop()


# Queue is FIFO
class Queue:
    def __init__(self):
        self._queue = list()

    def enqueue(self, data):
        self._queue.append(data)

    def dequeue(self):
        if not self._queue:
            return None
        else:
            return self._queue.pop(0)  # here, we are giving argument '0' to retrieve item from beginning of the list

print('Queue')
my_queue = Queue()
for a in range(10):
    my_queue.enqueue(a)

x = my_queue.dequeue()
print(type(x))
while x is not None: # here why we are writing "is not None" because x in while loop only can take numbers 1 to infinity
    # "x is not None" means x doesn't accept 0 and None. It accepts 1 to infinity numbers
    # for "while x", since x is type int, it will first get value 0 and doesn't go to while loop and later exits
    print(x)
    x = my_queue.dequeue()

print('Stack')
my_stack = Stack()
for item in range(10):
    my_stack.push(item)

b = my_stack.pop()
while b:
    print(b)
    b = my_stack.pop()