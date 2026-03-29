package fr.epita.tests.file;

import fr.epita.datamodel.Biotech;
import fr.epita.services.ArithmeticService;
import fr.epita.services.CSVService;

import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.List;

import java.util.Map;
import java.util.function.Function;

public class BiostatEntryReadingTest {
    public static void main(String[] args) throws FileNotFoundException {
        withFileAndScanner();
    }

    private static void withFileAndScanner() throws FileNotFoundException {
        String filePath = "./java-project/biostat/biostat.csv";
        List<Biotech> persons = CSVService.readFromFile(filePath);

        System.out.println(persons.size());


        Float averageAge = 0f;
        Float averageHeight = 0f;
        Float averageWeight = 0f;
        Integer minAge = 0;
        Integer maxAge = 0;

        for(Biotech person : persons){
            averageAge += person.getAge();
            averageHeight += person.getHeight();
            averageWeight += person.getWeight();

            minAge = Math.min(minAge, person.getAge());
            maxAge = Math.max(maxAge, person.getAge());
        }

        averageAge = averageAge / persons.size();
        averageHeight = averageHeight / persons.size();
        averageWeight = averageWeight / persons.size();

        System.out.println("Average Age: " + averageAge);
        System.out.println("Average Height: " + averageHeight);
        System.out.println("Average Weight: " + averageWeight);


        // Stream API -> Map Reduce
//        Double averageAge2 = persons.stream().mapToInt(Biotech::getAge).average();
//        Double averageAge3 = persons.parallelStream().mapToInt(Biotech::getAge).average();

        //
//        Function<Biotech, Integer> f = person -> person.getAge();
//        Function<Biotech, Integer> f2 = Biotech::getAge;

        System.out.println(ArithmeticService.computeAverage(persons, Biotech::getAge));
        System.out.println(ArithmeticService.computeAverage(persons, Biotech::getHeight));
        System.out.println(ArithmeticService.computeAverage(persons, Biotech::getWeight));

        // totalAge += f.apply(person)


        // No.2

        Map<String, Integer> distribution = new HashMap<>();
        for (Biotech entry: persons){
            Integer i = distribution.get(entry.getGender());
            if (i == null){
                i = 1;
            }else {
                i++;
            }
            distribution.put(entry.getGender(), i);
        }

        System.out.println("Gender Distribution: " + distribution);

        System.out.println(ArithmeticService.computeDistribution(persons, Biotech::getGender));
    }


}
