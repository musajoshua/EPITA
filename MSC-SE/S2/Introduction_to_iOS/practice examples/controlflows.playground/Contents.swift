import UIKit

let intArray = [1, 2, 3, 4, 5]
let intArray2 = 1...5

print(intArray)
print(intArray2)

// For

for i in 1...5 {
    print(i)
}

intArray.forEach {index in
    print(index)
}

enum Beverage: CaseIterable {
    case coffee
    case tea
}

let beverages = Beverage.allCases

for case .coffee in beverages {
    print("there is a coffee")
}


var count = 4;

// while

while count < 3 {
    count += 1;
    print("I'm into the while loop!")
}

var otherCount = 4;

repeat {
    otherCount += 1;
    print("I'm into the repeat loop!")
} while otherCount < 3;

// Defer

var buffer: Int?

@MainActor func saveFile() {
    defer {
        buffer = nil
    }
    buffer = 1
    
}
