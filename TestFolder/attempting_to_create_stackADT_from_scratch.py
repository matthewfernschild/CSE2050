# Right now I'm learning about Abstract Data Types & Concrete Data Structures using Gemini & the UConn Data Structures book by Sheehy.
# He shows the code behind different data structures as classes, I want to try and code them from memory to see if I can figure it out just by using my notes on the different methods.
###################
# Data Structures:
###################

# Stack ADT

class ListStack():
    def __init__(self):
        self.L = []
    
    def push(self,item):
        self.item = item
        self.L.append(item)
    
    def pop(self):
        return self.L.pop(-1)

    def peek(self):
        return self.L[-1]
    
    def size(self):
        return len(self.L)
    
    def isempty(self):
        return len(self.L) == 0
    
banana = ListStack()
banana.push(2)
print(f"end of stack after pushing is: {banana.peek()}")
print(f"Stack is Empty: {banana.isempty()}")
banana.push(4)
print(f"end of stack after pushing is: {banana.peek()}")
banana.push(3)
print(f"popped number is: {banana.pop()}")
print(f"popped number is: {banana.pop()}")
print(f"end of stack after pushing is: {banana.peek()}")
print(f"popped number is: {banana.pop()}")
print(f"Stack is Empty: {banana.isempty()}")

# i misremembered how he did isempty, but besides that I got it to work without help from the textbook