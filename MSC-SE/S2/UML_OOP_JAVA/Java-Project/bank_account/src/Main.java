import fr.epita.datamodel.*;
import fr.epita.services.AccountLogicService;

import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        // create a scenario where a customer called Quentin wants to buy 1 stock of gold
        // create the required investment account with a sufficient balance
        // when the operation is created, the balance is updated (minus the cost of the operation)
        // then Quentin decides to open a savings account and to initialize the balance to 3000E
        // what will be the earned interest over 1 year if the doesn't change the balance

        System.out.println("Welcome to bank!");

        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter your name");
        // Create Customer Quentin
        String name = scanner.nextLine();
        Customer customer = new Customer();
        customer.setName(name);

        // Create Stock GOLD
        System.out.println("Enter the stock ticker sign");
        String ticker = scanner.nextLine();
        System.out.println("Enter the stock price");
        Double stockPrice = scanner.nextDouble();
        Stock stock = new Stock(ticker, stockPrice);

        // Create investment account for customer
        System.out.println("Enter the initial deposit balance for the investment account");
        Double initialInvestmentAccountBalance = scanner.nextDouble();

        InvestmentAccount investmentAccount = new InvestmentAccount();
        investmentAccount.setAccountNumber("123456789");
        investmentAccount.setCustomer(customer);
        investmentAccount.setBalance(initialInvestmentAccountBalance);

        // Read quantity from user
        System.out.println("Enter the quantity to buy");
        double stockQuantity = scanner.nextDouble();


        // Account Servic Logic
        StockOrder stockOrder = AccountLogicService.buyStockFromAccount(stock, stockQuantity, investmentAccount);

        // Create a savings account
        System.out.println("Enter the initial deposit balance for the savings account");
        Double initialSavingsAccountBalance = scanner.nextDouble();

        SavingsAccount savingsAccount = new SavingsAccount();
        savingsAccount.setBalance(initialSavingsAccountBalance);
        savingsAccount.setAccountNumber("987654321");
        savingsAccount.setCustomer(customer);


        // TODO: Extract out of data model
        AccountLogicService.computeInterests(savingsAccount, 1);

        System.out.println("final balances: \n - investment " + + investmentAccount.getBalance() + "\n - savings " + savingsAccount.getBalance());





    }
}