"""
circle_queue
isFull : (rear + 1)%maxSize == front
isEmpty rear == front
size: (rear + maxSize - front)%maxSize
"""
class CircleQueue:
    def __init__(self,maxSize):
        self.queue =[None]*maxSize
        self.maxSize =maxSize
        self.front = 0 #public attr
        self.rear = 0
    def queueSize(self):
        return (self.rear - self.front + self.maxSize) %self.maxSize
    def isFull(self):
        return (self.rear + 1) % self.maxSize == self.front
    def isEmpty(self):
        return self.rear == self.front
    def addQueue(self,n):
        if self.isFull():
            print("Queue is full now, data cannot be added.")
            return
        self.queue[self.rear] = n
        self.rear = (self.rear + 1) % self.maxSize
    def getQueue(self):
        if self.isEmpty():
            print("queue is empty, cannot get data")
            return
        res = self.queue[self.front]
        self.front = (self.front + 1) % self.maxSize
        return res
    def showQueue(self):
        if self.isEmpty():
            print("queue is empty!")
            return
        for i  in range(self.front, self.front + self.queueSize()):
            print("arr[%d] = %d \n" %(i%self.maxSize, self.queue[(i% self.maxSize)]))
    def headQueue(self):
        if self.isEmpty():
            print("queue is empty")
        return self.queue[self.front]

q= CircleQueue(3)
q.addQueue(1)
q.addQueue(2)
q.addQueue(3)
print("show the queue:")
q.showQueue()

        





