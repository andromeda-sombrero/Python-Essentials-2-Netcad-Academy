"""
Lab Exercise 3 - Extending Queue Capabilities

Your task is to slightly extend the Queue class's capabilities.
We want it to have a parameterless method that returns True if the queue
is empty and False otherwise.
"""


class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.__queue_list = []

    def put(self, elem):
        return self.__queue_list.insert(0, elem)

    def get(self):
        if not len(self.__queue_list):
            raise QueueError

        val = self.__queue_list[-1]
        del self.__queue_list[-1]
        return val

    def isempty(self):
        if len(self.__queue_list) != 0:
            return False

        return True


class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)

for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
