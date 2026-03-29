package fr.epita.geometry.datamodel;

public class Square implements Shape {
    Rectangle rectangle;

    public Square(double side) {
        this.rectangle = new Rectangle(side, side);
    }

    public double calculateArea() {
        return rectangle.calculateArea();
    }

    public double calculatePerimeter() {
        return rectangle.calculatePerimeter();
    }


    public void setSide(double side) {
        rectangle.setWidth(side);
        rectangle.setHeight(side);
    }

    public double getSide() {
        return rectangle.getWidth();
    }

}
