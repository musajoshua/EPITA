package fr.epita.tests.file;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Scanner;

public class FileReadingTest {


    public static void main(String[] args) throws IOException {
        withFileAndScanner();

        // withPathApi();

    }

    private static void withPathApi() throws IOException {
        List<String> lines = Files.readAllLines(Path.of("biostat.csv"));
    }

    private static void withFileAndScanner() throws FileNotFoundException {
        File file = new File("biostat/biostat.csv");
        Scanner scanner = new Scanner(file);
        while (scanner.hasNext()){
            String currentLine = scanner.nextLine();
            System.out.println(currentLine);
            String[] parts = currentLine.split(",");
            for(String part : parts){
                System.out.println(part.trim());
            }
        }
    }
}