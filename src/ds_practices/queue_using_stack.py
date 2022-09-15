class Queue():
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, element):
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1]) # move all elements from s1 to s2
            self.s1.pop()

        self.s1.append(element)

        while(len(self.s2)) !=0 :
            self.s1.append(self.s2[-1])
            self.s2.pop()

        
    def dequeue(self):
        if len(self.s1) == 0: return None

        element = self.s1[-1]
        self.s1.pop()

        return element

class Queue2():
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, element):
        self.s1.append(element)

    def dequeue(self):
        if (len(self.s1) == 0 and len(self.s2) == 0):
            return None
        
        if len(self.s2) == 0 and len(self.s1) > 0:
            while(len(self.s1)):
                tmp = self.s1.pop()
                self.s2.append(tmp)
            return self.s2.pop()
        else:
            return self.s2.pop()

q = Queue()
q.enqueue(1)
q.enqueue(3)
q.enqueue(2)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())