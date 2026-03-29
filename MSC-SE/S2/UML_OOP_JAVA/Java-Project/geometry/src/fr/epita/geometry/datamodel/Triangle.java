package fr.epita.geometry.datamodel;

public class Triangle implements Shape {
    private double sideA;
    private double sideB;
    private double base;
    private double height;


    public Triangle(double base, double height, double sideA, double sideB) {
        this.sideA = sideA;
        this.sideB = sideB;
        this.base = base;
        this.height = height;
    }

    public double calculateArea(){
        return 0.5 * base * height;
    }

    public double calculatePerimeter(){
        return sideA + sideB + base;
    }
}
