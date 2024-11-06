import java.util.Scanner;
import java.util.Arrays;
import java.util.Collections;

public class Main {

    public static void sortArr(String[] arr){
        Arrays.sort(arr);

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        String[] arr = new String[n];

        for(int i=0; i<n; i++){
            arr[i] = sc.next();
        }

        sortArr(arr);

        for(int i=0; i<n; i++){
            System.out.println(arr[i]);
        }


        // 여기에 코드를 작성해주세요.
    }
}