import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] arr = new int[n];
        int[] narr = new int[n];

        for(int i=0; i<n; i++){
            int x = sc.nextInt();
            arr[i] = x*x;
        }

        for(int i=0; i<n; i++){
            System.out.printf("%d ",arr[i]);
        }


        // 여기에 코드를 작성해주세요.
    }
}