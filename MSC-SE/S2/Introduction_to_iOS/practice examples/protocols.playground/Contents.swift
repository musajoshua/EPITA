import UIKit

protocol Shape {
    func area() -> Double
}

struct Circle: Shape {
    let radius: Double
    
    func area() -> Double {
        return .pi * radius * radius
    }
}

struct Rectangle: Shape {
    let length: Double
    let breath: Double
    
    func area() -> Double {
        return length * breath
    }
}

func makeShape() -> Shape {
//    Circle(radius: 10)
    Rectangle(length: 10, breath: 25)
}
