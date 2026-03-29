package fr.epita.datamodel;

public class SavingsAccount extends Account {
    private Double interestRate;

    public Double getInterestRate() {
        return this.interestRate;
    }

    public void setInterestRate(Double interestRate) {
        this.interestRate = interestRate;
    }
}
