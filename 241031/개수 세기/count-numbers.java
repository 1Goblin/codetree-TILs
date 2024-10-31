import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int cnt = 0;

        int[] arr = new int[n];

        for(int i=0; i<n; i++){
            arr[i] = sc.nextInt();
        }

        for(int i=0; i<n; i++){
            if(arr[i] == m){
                cnt++;
            }
        }

        System.out.println(cnt);
        // 여기에 코드를 작성해주세요.
    }
}