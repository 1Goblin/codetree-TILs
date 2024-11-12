import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();

        int ansMax = Integer.MIN_VALUE;

        int[] arr = new int[n];

        for(int i=0; i<n; i++){
            arr[i] = sc.nextInt();
        }
        
        for(int i=0; i<=n-k; i++){
            int sum = 0;
            for(int j=i; j<i+k; j++){
                sum+=arr[j];
            }
            ansMax = Math.max(sum, ansMax);
        }

        System.out.println(ansMax);
        // 여기에 코드를 작성해주세요.
    }
}