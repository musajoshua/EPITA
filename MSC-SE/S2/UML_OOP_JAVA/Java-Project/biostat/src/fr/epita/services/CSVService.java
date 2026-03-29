package fr.epita.services;

import fr.epita.datamodel.Biotech;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class CSVService {
    public static List<Biotech> readFromFile(String filePath) throws FileNotFoundException {
        File file = new File(filePath);

        Scanner scanner = new Scanner(file);

        List<Biotech> persons = new ArrayList<Biotech>();

        // Array -> Mostly like tuple, fixed length
        // List is more suitable for array, growing length


        // Skip header
        scanner.nextLine();

        while(scanner.hasNext()){
            String currentLine = scanner.nextLine();

            String[] parts = currentLine.split(",");

            String name = parts[0].trim();
            String gender = parts[1].trim();
            Integer age = Integer.parseInt(parts[2].trim());
            Integer height = Integer.parseInt(parts[3].trim());
            Integer weight = Integer.parseInt(parts[4].trim());

            Biotech person = new Biotech(name, gender, age, height, weight);

            persons.add(person);
        }
        return persons;
    }
}
