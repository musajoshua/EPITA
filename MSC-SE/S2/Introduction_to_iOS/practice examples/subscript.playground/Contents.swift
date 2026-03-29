struct Week {
    let days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    
    subscript(index: Int) -> String {
        days[index]
    }
}

let week = Week()

print(week[2])

struct WeekDictionary {
    enum Week: String {
        case monday
        case tuesday
        case wednesday
    }
    
    func humorOfTheDay(weekDay: Week) -> String {
        switch weekDay {
            case .monday:
                "Not cool but there is iOS class so nice"
            
            
            case .tuesday, .wednesday:
                "Near the week end"
            
        }
    }
    
    subscript(key: String) -> String {
        return humorOfTheDay(weekDay: .init(rawValue: key) ?? .monday)
    }
}


let weekDictionary = WeekDictionary()

print(weekDictionary["monday"])
