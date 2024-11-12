import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int[] arr = new int[n];

        for(int i=0; i<n; i++){
            arr[i] = sc.nextInt();
        }

        int minAbs = Integer.MAX_VALUE;

        for(int i=0; i<n; i++){
            int ans = 0;
            for(int j=0; j<n; j++){
                ans += arr[j] * Math.abs(j-i);
            }
            if(minAbs > ans){
                minAbs = ans;
            }
        }

        System.out.println(minAbs);
        

        // 여기에 코드를 작성해주세요.
    }
}