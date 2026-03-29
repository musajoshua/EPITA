package fr.epita.datamodel;

public class Stock {
    private String ticker;
    private Double currentPrice;

    public Stock() {
    }

    public Stock(String ticker, Double price) {
        this.ticker = ticker;
        this.currentPrice = price;
    }

    public String getTicker() {
        return this.ticker;
    }

    public void setTicker(String ticker) {
        this.ticker = ticker;
    }

    public Double getCurrentPrice() {
        return this.currentPrice;
    }

    public void setCurrentPrice(Double currentPrice) {
        this.currentPrice = currentPrice;
    }
}
