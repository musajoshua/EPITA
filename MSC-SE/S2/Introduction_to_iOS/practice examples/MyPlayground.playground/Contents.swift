import UIKit

// let is immutable
let name = "Joshua"

// var is mutable
var epitaId = 52

var studentDescription: String {
    "\(name) student id is \(epitaId)"
}

print(studentDescription)
epitaId = 3
print(studentDescription)

//funct br

typealias EpitaID = Int;

func search(by epitaId: EpitaID){
    
}

//String
//Int
//Float
//Double
//Bool

// Function

func search(by epitaId: Int, name: String){
    print(epitaId);
}

search(by: 52, name: "Joshua")

// Anonymous param
func searchByEpitaId(_ epitaId: Int){
    print(epitaId);
}

searchByEpitaId(epitaId)

// default value
func searchById(_ epitaId: Int = 0){
    print(epitaId);
}

searchById(50)

// In out parameter
var myNumber = 0;

func increaseByOne(p: inout Int){
    p += 1
}

increaseByOne(p: &myNumber)
print(myNumber)


// Class
class Animal {
    var size: CGSize
    
    init(size: CGSize){
        self.size = size
    }
}

class Dog: Animal {
    
}

//let myDog = Dog(size: .init(width: 10, height: 5))
//let myDog = Dog.init(size: (width: 10, height: 5))

let myDog: Dog = .init(size: .init(width: 10, height: 5))


// Override - replace parents class behaviour
// Super - call parents class behaviour
// final - block inheritance


class Car {
    var brand: String
    var maxSpeed: Int {
        200
    }
    
    init(brand: String) {
        self.brand = brand
    }
    
    func description() -> String {
        return "\(brand) can go up to \(maxSpeed) km/h"
    }
}

class ElectricCar: Car {
    override var maxSpeed: Int {
        300
    }
}

class ThermicalCar: Car {
    override var maxSpeed: Int {
        100
    }
}

var tesla: ElectricCar = .init(brand: "Tesla")
var peugot: ThermicalCar = .init(brand: "Peugeot")

let cars: [Car] = [tesla, peugot]

cars.forEach { car in
    print(car.maxSpeed)
}

for car in cars {
    print(car.maxSpeed)
}


