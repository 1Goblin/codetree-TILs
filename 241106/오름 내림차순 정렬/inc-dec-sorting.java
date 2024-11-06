import java.util.Scanner;
import java.util.Arrays;
import java.util.Collections;

public class Main {
    public static void sortArr(Integer[] arr){
        Arrays.sort(arr);
    }

    public static void reverseSortArr(Integer[] arr){
        Arrays.sort(arr, Collections.reverseOrder());
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        Integer n = sc.nextInt();

        Integer[] arr = new Integer[n];


        for(int i=0; i<n; i++){
            arr[i] = sc.nextInt();
        }

        sortArr(arr);
        
        for(int i=0; i<n; i++){
            System.out.printf("%d ", arr[i]);
        }
        System.out.println();

        reverseSortArr(arr);

        for(int i=0; i<n; i++){
            System.out.printf("%d ", arr[i]);
        }




        // 여기에 코드를 작성해주세요.
    }
}