package fr.epita.services;

import fr.epita.datamodel.InvestmentAccount;
import fr.epita.datamodel.SavingsAccount;
import fr.epita.datamodel.Stock;
import fr.epita.datamodel.StockOrder;

public class AccountLogicService {
    private static final double COMMISSION_RATE = 0.10;
    public static final double DEFAULT_INTEREST_RATE = 0.08;

    public static StockOrder buyStockFromAccount (Stock stock, Double quantity, InvestmentAccount investmentAccount){
        Double price = stock.getCurrentPrice();
        Double commission = COMMISSION_RATE * quantity * price;

        investmentAccount.setBalance(investmentAccount.getBalance() - commission - quantity * price);

        StockOrder stockOrder = new StockOrder();
        stockOrder.setStock(stock);
        stockOrder.setInvestmentAccount(investmentAccount);
        stockOrder.setQuantity(quantity);
        stockOrder.setUnitPrice(price);

        stockOrder.setCommission(commission);

        return stockOrder;
    }

    public static Double calculateInterest(SavingsAccount savingsAccount, Integer time){
        return savingsAccount.getBalance() * savingsAccount.getInterestRate() * time;
    };

    public static void computeInterests(SavingsAccount savingsAccount, Integer time){
        Double interestRate = DEFAULT_INTEREST_RATE;
        savingsAccount.setInterestRate(interestRate);
        Double balance = savingsAccount.getBalance();
        Double interest = AccountLogicService.calculateInterest(savingsAccount, time);
        savingsAccount.setBalance(balance + interest);
    }
}
