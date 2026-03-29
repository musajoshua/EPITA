//
//  MoneyTrackerApp.swift
//  MoneyTracker
//
//  Created by Joshua Musa on 23/03/2026.
//

import SwiftUI

@main
struct MoneyTrackerApp: App {
    var body: some Scene {
        WindowGroup {
            ExpensesView(expensesViewModel: .init())
        }
    }
}
