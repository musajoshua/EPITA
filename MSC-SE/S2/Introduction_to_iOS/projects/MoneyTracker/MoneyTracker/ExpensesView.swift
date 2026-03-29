//
//  ExpensesView.swift
//  MoneyTracker
//
//  Created by Joshua Musa on 23/03/2026.
//

import SwiftUI

struct ExpensesView: View {
    
    @ObservedObject var expensesViewModel : ExpensesViewModel
    var body: some View {
        Text("Hello world!")
        
        NavigationView {
            List {
                ForEach(expensesViewModel.expenses) { expense in
                    HStack {
                        Text(expense.name)
                        Text(expense.amount.description).bold()
                    }
//                    .font(.title)
                }
                .onDelete(perform: withAnimation {
                    expensesViewModel.deleteExpense(offsets:)
                })

            }
            .navigationTitle("Expenses")
        }
        
//        ScrollView {
//            VStack {
//                
//            }
//        }
    }
}

//# if DEBUG
//        
//# Endif


#Preview {
    ExpensesView(expensesViewModel: .init())
}
