import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        
        int[][] arr = new int[n][n];

        for(int i=0; i<m; i++){
            int r,c;
            r = sc.nextInt()-1;
            c = sc.nextInt()-1;

            arr[r][c] = 1;
        }

        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
        // 여기에 코드를 작성해주세요.
    }
}