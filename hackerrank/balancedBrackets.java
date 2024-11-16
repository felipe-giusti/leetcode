import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'isBalanced' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts STRING s as parameter.
     */

    public static String isBalanced(String s) {
        Map<Character, Character> openCloseMapping = new HashMap<>();
        openCloseMapping.put('{', '}');
        openCloseMapping.put('[', ']');
        openCloseMapping.put('(', ')');
        
        Stack<Character> charStack = new Stack<>();
        
        for(char c : s.toCharArray()){
            if (openCloseMapping.containsKey(c)){
                charStack.push(openCloseMapping.get(c));
            }else{
                if (charStack.isEmpty() || c != charStack.pop()){
                    return "NO";
                }
            }
        }
        return charStack.isEmpty()? "YES" : "NO";
        
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int t = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, t).forEach(tItr -> {
            try {
                String s = bufferedReader.readLine();

                String result = Result.isBalanced(s);

                bufferedWriter.write(result);
                bufferedWriter.newLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();
        bufferedWriter.close();
    }
}
