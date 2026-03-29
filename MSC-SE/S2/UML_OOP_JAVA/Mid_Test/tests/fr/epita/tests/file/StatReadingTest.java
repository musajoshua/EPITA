package fr.epita.tests.file;

import fr.epita.datamodel.Person;
import fr.epita.service.CSVService;
import fr.epita.service.StatService;

import java.io.FileNotFoundException;
import java.util.List;

public class StatReadingTest {
    public static void main(String[] args) throws FileNotFoundException {
        withFileAndScanner();
    }

    private static void withFileAndScanner() throws FileNotFoundException {
        String filePath = "./data.csv";
        List<Person> persons = CSVService.readFromFile(filePath);


        System.out.println("Average Age " + StatService.computeAverage(persons, Person::getAge));
        System.out.println("Gender Distribution " + StatService.computeDistribution(persons, Person::getSex));
        System.out.println("Male Distribution " + StatService.computeDistribution(persons, Person::getSex).get("male"));
        System.out.println("Female Distribution " + StatService.computeDistribution(persons, Person::getSex).get("female"));



    }
}
