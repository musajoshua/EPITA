import UIKit

struct User {
    private let id: String
    private(set) var mood: String = "Nice"
    
    let name: String
    
    init(name: String) {
        self.name = name
        id = "\(name)-id"
        mood = "Cool"
    }
}

let user = User(name: "John")

print(user.name)
print(user.mood)
//user.mood = "Happy"
//print(user.id)

private extension User {
    func printName() {
        print(self.name)
    }
    
    func setMood(_ newMood: String) {
        self.mood = newMood
    }
}
≥

user.printName()
