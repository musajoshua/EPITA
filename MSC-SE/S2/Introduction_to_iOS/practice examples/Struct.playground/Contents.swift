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
    let firstName: String;
    let lastName: String;
    var age: Int;
    
//    init(firstName: String, lastName: String, age: Int) {
//        self.firstName = firstName
//        self.lastName = lastName
//        self.age = age
//    }
}

let personClass = PersonClass(firstName: "John", lastName: "Snow", age: 30)

let personStruct = PersonStruct(firstName: "John", lastName: "Snow", age: 30)

var personClass2 = personClass
var personStruct2 = personStruct

personClass2.age = 27
personStruct2.age = 27


print("Class original and copy", personClass.age, personClass2.age)
print("Struct original and copy", personStruct.age, personStruct2.age)

