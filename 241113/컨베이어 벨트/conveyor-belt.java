import java.util.*;

public class Main {

    public static int t;
    public static int n;

    public static void move(int[] arr){
        int m = 2*n;
        int temp = arr[m-1];

        for(int i=m-1; i>0; i--){
            arr[i] = arr[i-1];
        }
        arr[0] = temp;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        t = sc.nextInt();

        int[] arr = new int[2*n];

        for(int i=0; i<n*2; i++){
            arr[i] = sc.nextInt();
        }

        for(int i=0; i<t; i++){
            move(arr);
        }

        for(int i=0; i<n; i++){
            System.out.printf("%d ", arr[i]);
        }

        System.out.println();

        for(int i=n; i<2*n; i++){
            System.out.printf("%d ",arr[i]);
        }

        // 여기에 코드를 작성해주세요.
    }
}