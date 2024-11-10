import java.util.Scanner;

public class Main {
    public static int OFFSET = 100;

    public static void createBlock(int[] arr, int a, int b){


        
        for(int i=a; i<b; i++){
            arr[i] += 1;
        }
    }

    public static int findans(int[] arr){
        int max = 0;

        for(int i=0; i<arr.length; i++){
            if(max<arr[i]){
                max = arr[i];
            }
        }

        return max;

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int[] arr = new int[200];

        for(int i=0; i<n; i++){
            int x1 = sc.nextInt();
            int x2 = sc.nextInt();

            createBlock(arr, x1+OFFSET, x2+OFFSET);
        }


        System.out.println(findans(arr));



        // 여기에 코드를 작성해주세요.
    }
}