import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class Pattern {
    private static int readSize(String fileName) throws IOException {
        String text = Files.readString(Path.of(fileName)).trim();
        if (text.contains("=")) {
            text = text.split("=", 2)[1].trim();
        }

        int size = Integer.parseInt(text);
        if (size <= 0) {
            throw new IllegalArgumentException("pattern size must be positive");
        }
        return size;
    }

    private static String makePattern(int size) {
        StringBuilder pattern = new StringBuilder();
        for (int row = 1; row <= size; row++) {
            pattern.append(" ".repeat(size - row));
            pattern.append("*".repeat(2 * row - 1));
            if (row < size) {
                pattern.append(System.lineSeparator());
            }
        }
        return pattern.toString();
    }

    public static void main(String[] args) throws IOException {
        if (args.length == 0) {
            System.out.println("Usage: java Pattern <parameter-file> [parameter-file ...]");
            return;
        }

        for (int index = 0; index < args.length; index++) {
            int size = readSize(args[index]);
            if (index > 0) {
                System.out.println();
            }
            System.out.println(args[index] + " -> size " + size);
            System.out.println(makePattern(size));
        }
    }
}
