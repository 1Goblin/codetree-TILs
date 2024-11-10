import java.util.*;

public class Main {
    public static void createBlock(int[] arr, int a, int b){

        for(int i=a-1; i<b; i++){
            arr[i] += 1;
        }

    }

    public static int showMaxBlock(int[] arr){

        int max = -1;

        for(int i=0; i<arr.length; i++){
            if(max < arr[i]){
                max = arr[i];
            }
        }

        return max;

    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();

        int[] arr = new int[n];

        for(int i=0; i<k; i++){
            int a = sc.nextInt();
            int b = sc.nextInt();

            createBlock(arr, a, b);
        }

        System.out.println(showMaxBlock(arr));


        // 여기에 코드를 작성해주


    }
}