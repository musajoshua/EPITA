import UIKit

class Car {
    var brand: String
    var maxSpeed: Int { 200 }
    
    init(brand: String) {
        self.brand = brand
    }
    
    func description() -> String {
        return "\(brand) can go up to \(maxSpeed)"
    }
}

final class ElectricCar: Car {
    override var maxSpeed: Int { 300 }
}

class ThermicalCar: Car {
    override var maxSpeed: Int { 100 }
}

var tesla: ElectricCar = .init(brand: "Tesla")
var peugeot: ThermicalCar = .init(brand: "Peugeot")

let cars: [Car] = [tesla, peugeot]
cars.forEach { car in
    print("\(car.maxSpeed)")
}
