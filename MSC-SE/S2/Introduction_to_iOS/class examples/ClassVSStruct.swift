import UIKit

class PersonClass {
    let firstName: String
    let lastName: String
    var age: Int
    
    init(firstName: String, lastName: String, age: Int) {
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
    }
}

struct PersonStruct {
    let firstName: String
    let lastName: String
    var age: Int
}

let personClass = PersonClass(firstName: "Antoine", lastName: "L.", age: 31)
var personStruct = PersonStruct(firstName: "Antoine", lastName: "L.", age: 31)

let personClass2 = personClass
var personStruct2 = personStruct

personClass2.age = 32

personStruct.age = 32
print(personStruct2.age)
