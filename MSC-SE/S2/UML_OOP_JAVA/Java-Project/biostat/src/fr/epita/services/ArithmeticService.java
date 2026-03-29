package fr.epita.services;

import fr.epita.datamodel.Biotech;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.function.Function;

public class ArithmeticService {

    public static Map<String, Integer> computeDistribution(List<Biotech> entries, Function<Biotech, String> f){
        Map<String, Integer> distribution = new HashMap<>();
        for (Biotech entry: entries){
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

    public static double computeAverage(List<Biotech> entries, Function<Biotech, Integer> f) {
        double total = 0;
        for(Biotech entry : entries){
            total += f.apply(entry);
        }
        return total / entries.size();
    }
}
