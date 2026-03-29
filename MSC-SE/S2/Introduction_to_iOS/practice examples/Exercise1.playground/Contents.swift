import UIKit

class Person {
    var id: String
    var firstName: String
    var lastName: String
    var age: Int
    
    var computedId: String {
        id
    }
    
    var fullName: String {
        "\(firstName) \(lastName)"
    }
    
    func shortDescription() -> String {
        return ("The id is \(id). The computed id is \(computedId). The fullname is \(fullName). The age is \(age) years old.")
    }
    
    init(id: String, firstName: String, lastName: String, age: Int) {
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
    }
}

final class EPITAStudent: Person {
    var averageRating: Double;
    
    override var computedId: String {
        "COMPUTED-\(super.id)"
    }
    
    override func shortDescription() -> String {
        return ("The student average rating is \(averageRating). \(super.shortDescription())")
    }
    
    func celebratesBirthday(){
        age += 1
    }
    
    init(id: String, firstName: String, lastName: String, age: Int, averageRating: Double) {
        self.averageRating = averageRating
        super.init(id:"EPITA-\(id)", firstName: firstName, lastName: lastName, age: age)
    }
    
}

var person1: Person = .init(id: "123", firstName: "Joshua", lastName: "Musa", age: 20)
var student1: EPITAStudent = .init(id: "123", firstName: "Joshua", lastName: "Musa", age: 20, averageRating: 19.5)

let persons: [Person] = [person1, student1]

for person in persons {
    print(person.shortDescription())
}

student1.celebratesBirthday()
print(student1.shortDescription())
