import UIKit

// Arrays

let daysOfTheWeek: [String] = ["Mon", "Tue"]

//let daysOfTheWeek: [Any] = ["Mon", "Tue", 2, 3.4]

// Use as? to type cast => print(daysWithAny[2] as? Int)


daysOfTheWeek.contains { value in
    value == "Mon"
//    value as? String == "Mon
}

daysOfTheWeek.isEmpty


// Sets

struct Fruit: Hashable {
    let name: String
}


let fruitBasket: Set<Fruit> = [
    .init(name: "Strawberry"),
    .init(name: "Apple"),
    Fruit(name: "Banana")
]

print(fruitBasket)
print(fruitBasket)
print(fruitBasket)

// No order in fruit basket
// Cannot access with normal index
// fruitBasket[0]

print(fruitBasket.contains(.init(name: "Banana")))


// Dictionaries
var fruitWithPrice: [String: Int] = [
    "Apple": 2,
    "Strawberry": 3,
    "Banana": 100
]

print(fruitWithPrice)

print(fruitWithPrice["Apple"])


fruitWithPrice["Apple"] = 3
fruitWithPrice["Orange"] = 1000


print(fruitWithPrice)

fruitWithPrice.removeValue(forKey: "Banana")

print(fruitWithPrice)

fruitWithPrice["Apple"] = nil

print(fruitWithPrice)


