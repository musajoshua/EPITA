import UIKit

class Stack<T> {
    var stack: [T]
    
    var isEmpty: Bool {
        stack.isEmpty
    }
    
    func push(newElement: T){
        stack.append(newElement)
    }
    
    func pop() -> T? {
        if (isEmpty) {
            return nil
        }
        let lastElement = stack.removeLast();
        return lastElement
    }
    
    init() {
        self.stack = []
    }
    
}

var newStack = Stack<Int>()

print("Stack is empty ? ", newStack.isEmpty)

newStack.push(newElement: 1)
newStack.push(newElement: 2)



print("Stack is empty ? ", newStack.isEmpty)

print("Stack : ", newStack)

if let topElement = newStack.pop() {
    print("Popped element : ", topElement)
}
 
newStack.push(newElement: 3)
print("Stack : ", newStack)

