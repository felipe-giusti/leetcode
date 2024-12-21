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
     * Complete the 'miniMaxSum' function below.
     *
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static void miniMaxSum(List<Integer> arr) {
        int i_min = 0, i_max = 0;
        long sum = arr.get(0);
        
        for (int i=1; i<arr.size(); i++){
            sum += arr.get(i);
            if (arr.get(i) < arr.get(i_min)){
                i_min = i;
            }else if (arr.get(i) > arr.get(i_max)){
                i_max = i;
            }
        }
        long minSum = sum - arr.get(i_max);
        long maxSum = sum - arr.get(i_min);
        System.out.println(minSum + " " + maxSum);
    }
}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        Result.miniMaxSum(arr);

        bufferedReader.close();
    }
}
