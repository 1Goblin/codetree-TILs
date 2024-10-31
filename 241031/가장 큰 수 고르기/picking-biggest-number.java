import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        final int INT_MIN = Integer.MIN_VALUE;
        Scanner sc = new Scanner(System.in);
        int ans = INT_MIN;

        int[] arr = new int[10];

        for(int i=0; i<10; i++){
            arr[i] = sc.nextInt();
        }

        for(int i=0; i<10; i++){
            if(arr[i]> ans){
                ans = arr[i];
            }
        }

        System.out.println(ans);
        // 여기에 코드를 작성해주세요.
    }
}