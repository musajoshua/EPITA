import UIKit

enum Cocktail {
    case mojito
    case expressoMartini
}

let inHappyHour = true

enum Beverage {
    case coffee
    case tea
    case juice
    case beer
    case cocktail(cocktailName: String)
}

let myBeverage = Beverage.cocktail(cocktailName: "ExpressoMartini")

if case Beverage.cocktail(let cocktailName) = myBeverage {
    print(cocktailName)
}
/*
 "beverage": "coffee"
 
 */

enum SpeedLimit: Int, RawRepresentable {
    case highway = 130
    case city = 50
}


var carSpeed = 100

switch carSpeed {
case (0...100):
    print("low speed")
case (100...130):
    print("becareful")
default:
    print("call the police")
}
