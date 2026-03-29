//
//  ExpensesViewModel.swift
//  MoneyTracker
//
//  Created by Joshua Musa on 23/03/2026.
//

import SwiftUI
import Combine

final class ExpensesViewModel: ObservableObject {
    @Published var expenses: [Expense] = [
        .init(id: .init(), name: "McDo", amount: 25, date: .now),
        .init(id: .init(), name: "Steam", amount: 80, date: .now),
        .init(id: .init(), name: "Bar", amount: 15, date: .now),
    ]
    
    func deleteExpense(offsets: IndexSet) {
        for index in offsets {
            expenses.remove(at: index)
        }
    }
}
