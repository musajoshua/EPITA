import UIKit

enum Cocktail {
    case mojito
    case expressoMartini
}

let inHappyHour = true

enum Beverage: CaseIterable {
    static let volume = 100
    
    case coffee
    case tea
    case juice
    case beer
    case cocktail(Cocktail)
//    case soda
    
    var price: Int {
        switch self {
        case .coffee:
            return 2
        case .tea, .juice, .beer:
            return 3
//        case .cocktail(let cocktail) where
//            cocktail == .expressoMartini
//            return 4
        case .cocktail where inHappyHour:
            return 8
        case .cocktail:
            return 10
//        default:
//            return 5
        
        }
    }
}


let coffeeBeverage: Beverage = .coffee

let allBeverages = Beverage.allCases
