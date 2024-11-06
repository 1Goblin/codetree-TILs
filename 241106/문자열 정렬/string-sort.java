import java.util.Scanner;
import java.util.Arrays;
import java.util.Collections;

public class Main {

    public static String sortString(String a){
        char[] arr = a.toCharArray();

        Arrays.sort(arr);

        String newStr = new String(arr);

        return newStr;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();


        System.out.println(sortString(a));
        // 여기에 코드를 작성해주세요.
    }
}