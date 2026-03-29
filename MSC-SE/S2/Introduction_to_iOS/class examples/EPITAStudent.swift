
class Person {
    let firstName: String
    let lastName: String
    let baseId: String
    var age: Int
    
    var id: String {
        baseId
    }
    
    var fullName: String {
        firstName + lastName
    }
    
    init(firstName: String, lastName: String, baseId: String, age: Int) {
        self.firstName = firstName
        self.lastName = lastName
        self.baseId = baseId
        self.age = age
    }
    
    func shortDescription() -> String {
        "\(fullName), \(age) years old"
    }
}

final class EpitaStudent: Person {
    var averageRating: Double
    
    override var id: String {
        "EPITA-\(super.baseId)"
    }
    
    init(firstName: String, lastName: String, baseId: String, age: Int, averageRating: Double) {
        self.averageRating = averageRating
        super.init(firstName: firstName, lastName: lastName, baseId: baseId, age: age)
    }
    
    override func shortDescription() -> String {
        super.shortDescription() + "EPITA average rating: \(averageRating)"
    }
}

func celebratesBirthday(for person: Person) {
    person.age += 1
}

let john = Person(firstName: "John", lastName: "Appleseed", baseId: "1234", age: 50)
let alice = EpitaStudent(firstName: "Alice", lastName: "Wonderland", baseId: "6789", age: 40, averageRating: 19.5)

var people: [Person] = [john, alice]

for person in people {
    print(person.shortDescription())
}

celebratesBirthday(for: alice)
print(alice.age)
