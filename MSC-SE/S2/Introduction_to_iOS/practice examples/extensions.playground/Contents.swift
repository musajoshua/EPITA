struct WeekDictionary {
    enum Week: String {
        case monday
        case tuesday
        case wednesday
    }
    
    subscript(key: String) -> String {
        return humorOfTheDay(weekDay: .init(rawValue: key) ?? .monday)
    }
}

extension WeekDictionary {
    func humorOfTheDay(weekDay: Week) -> String {
        switch weekDay {
            case .monday:
                "Not cool but there is iOS class so nice"
            
            
            case .tuesday, .wednesday:
                "Near the week end"
            
        }
    }
}

let weekDictionary = WeekDictionary()

print(weekDictionary["monday"])

extension Int {
    mutating func increaseByOne() {
        self += 1
    }
}

var number = 1

number.increaseByOne()
