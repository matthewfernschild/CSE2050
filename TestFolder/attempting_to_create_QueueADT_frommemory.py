# i wonder if i can do this 
# a queue is a list except we want to change the first place as opposed to the last place in a stack
# we can do this using a head as an additional variable
# uses enqueue, dequeue, peek, length, isempty

class QueueADT():
    def __init__(self):
        self.head = 0
        self.L = []

    def peek(self):
        try:
            return self.L[self.head]
    # this is my attempt at learning how to make error codes n stuff, ive used try and except maybe once before
        except IndexError:
            raise RuntimeError("peeked when nothing in queue yet")

    def enqueue(self,item):
        self.L.append(item)

    def dequeue(self):
        try:
            item = self.L[self.head]
            self.head += 1
            if self.head > len(self.L)//2:
                self.L = self.L[self.head:]
                self.head = 0
            return item
        except IndexError:
            raise RuntimeError("you can't dequeue an item when there is no item")
            
        
    def __len__(self): # using the __ on both sides updates pythons actual len() function for how to affect any object of this class I think, i didnt have to call meow.len(), i just used len() on the object and it got it correct.
        return len(self.L) - self.head
    
    def isempty(self):
        return len(self) == 0

meow = QueueADT()
meow.dequeue()
meow.enqueue(2)
meow.enqueue(3)
meow.enqueue(1)
meow.enqueue(5)

print(f"Length: {len(meow)}")
print(meow.dequeue())
print(f"Length: {len(meow)}")
print(meow.dequeue())
print(f"Length: {len(meow)}")
print(meow.dequeue())
print(f"Length: {len(meow)}")
print(meow.dequeue())
print(f"Length: {len(meow)}")
print(meow.isempty())

