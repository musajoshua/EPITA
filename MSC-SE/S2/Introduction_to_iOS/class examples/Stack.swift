struct Stack<Element> {
    var items: [Element] = []
    
    mutating func push(_ item: Element) {
        items.append(item)
    }
    
    mutating func pop() -> Element? {
        guard !isEmpty else { return nil }
        return items.removeLast()
    }
    
    var isEmpty: Bool { items.isEmpty }
}

var intStack = Stack<Int>()
intStack.push(1)
intStack.push(2)
intStack.push(3)

intStack.pop()
intStack.pop()
intStack.pop()
intStack.pop()
