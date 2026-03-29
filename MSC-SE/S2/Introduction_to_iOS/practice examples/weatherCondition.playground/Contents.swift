import UIKit

enum WeatherCondition: CaseIterable {
    case sunny
    case rainy
    case cloudy
    
    var emoji: String {
        switch self {
            case .sunny:
                return "☀️"
            case .cloudy:
                return "☁️"
            case .rainy:
                return "🌧️"
        }
    }
}

let currentWeather = WeatherCondition.cloudy
print(currentWeather.emoji)

func weatherMessage(for condition: WeatherCondition) -> String {
    switch condition {
        case .sunny:
            return "The weather is sunny"
        case .cloudy:
            return "The weather is cloudy"
        case .rainy:
            return "The weather is rainy"
    }
}

print(weatherMessage(for: currentWeather))

let randomWeather: WeatherCondition? = WeatherCondition.allCases.randomElement()
// kearn enums

//class WeatherConditionClass {
//    var emoji: Emoji
//    
//    init?(emoji: Emoji) {
//        if Emoji.sunny == emoji || Emoji.rainy == emoji || Emoji.clouy == emoji {
//            self.emoji = emoji
//        }else{
//            return nill
//        }
//    }
//    
//    func weatherMessage() -> String {
//        return "The weather is \(emoji)"
//    }
//}
//
//
//var todaysWeather: WeatherCondition?
