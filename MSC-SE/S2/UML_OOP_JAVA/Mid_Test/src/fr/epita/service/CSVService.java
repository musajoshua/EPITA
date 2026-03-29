package fr.epita.service;

import fr.epita.datamodel.Person;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class CSVService {

    public static List<Person> readFromFile(String filePath) throws FileNotFoundException {
        String DEFAULT_AGE = "0";
        File file = new File(filePath);

        Scanner scanner = new Scanner(file);

        List<Person> persons = new ArrayList<Person>();

        scanner.nextLine();

        while(scanner.hasNext()){
            String currentLine = scanner.nextLine();

            String[] parts = currentLine.split(";");

            String name = parts[0].trim();
            String pClass = parts[1].trim();
            Double age = Double.parseDouble(parts[2].trim().equals("") ? DEFAULT_AGE : parts[2].trim());
            String sex  = parts[3].trim();
            Integer survived = Integer.parseInt(parts[4].trim());

            Person person = new Person(name, pClass, age, sex, survived);

            persons.add(person);
        }
        return persons;
    }
}
