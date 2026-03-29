package fr.epita.geometry.executions;

import fr.epita.geometry.datamodel.Circle;
import fr.epita.geometry.datamodel.Rectangle;
import fr.epita.geometry.datamodel.Square;
import fr.epita.geometry.datamodel.Triangle;
import fr.epita.geometry.datamodel.Shape;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Main {
    public static void main (String[] args) {
        Square square = new Square(5);

        square.calculateArea();
        square.calculatePerimeter();

        Square square1 = new Square(10);

        Triangle triangle = new Triangle(3,4,5,6);
        Triangle triangle2 = new Triangle(30,40,50,60);

        Circle circle = new Circle(5);
        Circle circle2 = new Circle(10);

        Rectangle rectangle = new Rectangle(5, 6);
        Rectangle rectangle2 = new Rectangle(10, 12);


        Shape[] instances = { square, square1, triangle, triangle2, circle, circle2, rectangle, rectangle2 };

        double globalArea = 0;

        for (Shape instance : instances) {
//            if (instance instanceof shape){
//
//            }
            globalArea += instance.calculateArea();
        }

        List<String> list = List.of("a", "b", "c");
        List<String> list2 = new Stack<>();
        ArrayList<String> list3 = new ArrayList<>();

    }
}
