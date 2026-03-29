package fr.epita.service;

import fr.epita.datamodel.Person;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.function.Function;

public class StatService {

    public static Map<String, Integer> computeDistribution(List<Person> entries, Function<Person, String> f){
        Map<String, Integer> distribution = new HashMap<>();
        for (Person entry: entries){
            Integer i = distribution.get(f.apply(entry).toString());
            if (i == null){
                i = 1;
            }else {
                i++;
            }
            distribution.put(f.apply(entry).toString(), i);
        }

        return distribution;
    }

    public static double computeAverage(List<Person> entries, Function<Person, Double> f) {
        double total = 0;
        for(Person entry : entries){
            total += f.apply(entry);
        }
        return total / entries.size();
    }
}
