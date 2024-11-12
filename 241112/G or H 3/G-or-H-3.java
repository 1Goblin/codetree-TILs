import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt() +1 ;

        int[] arr = new int[9999];

        for(int i=0; i<n; i++){
            int index = sc.nextInt();
            char sign = sc.next().charAt(0);

            if(sign == 'G'){
                arr[index] = 1;
            } else if(sign == 'H'){
                arr[index] = 2;
            }

        }

        int ans = Integer.MIN_VALUE;

        for(int i=0; i<=arr.length - k; i++){
            int sum = 0;
            for(int j=i; j<i+k; j++){
                sum+=arr[j];
                
            }

            ans = Math.max(ans, sum);
        }


 

        System.out.println(ans);
    }
}