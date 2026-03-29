//
//  Expense.swift
//  MoneyTracker
//
//  Created by Joshua Musa on 23/03/2026.
//

import Foundation

struct Expense: Identifiable {
    let id: UUID
    let name: String
    let amount: Double
    let date: Date
}
