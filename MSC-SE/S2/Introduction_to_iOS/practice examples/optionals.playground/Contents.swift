

//enum Optional<T> {
//    case none
//    case value(T)
//}

var bankAmount: Int?
print(bankAmount)

// load bank data
//bankAmount = 100
print(bankAmount)

if let bankAmountWrapped = bankAmount {
    print(bankAmountWrapped)
}

if let bankAmount {
    print(bankAmount)
}

guard let bankAmount else {
    print("no bank amount value")
    return
}



// Nil Coalising
var userName: String?

let displayName: String = userNAme ?? "Guest"


let blacklist = ["Joshua"]

class EpitaStudent {
    let lastName: String
    
    init?(lastName: String) {
        guard !blacklist.contains ( where: { name in
            name == lastName
            
        }) else {
            self.lastName = lastName
        }
    }
}

let epitaStudents = EpitaStudent(lastName: "Joshua")
print(epitaStudents)
