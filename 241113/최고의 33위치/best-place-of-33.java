import java.util.*;

public class Main {

    public static int n;

    public static int checkCoin(int[][] arr, int x, int y){
        int cnt = 0;

        for(int i=x; i<x+3; i++){
            for(int j=y; j<y+3; j++){
                if(arr[i][j] == 1){
                    cnt++;
                }
            }
        }

        return cnt;

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();

        int maxCoin = Integer.MIN_VALUE;
        
        int[][] arr = new int[n][n];

        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                arr[i][j] = sc.nextInt();
            }
        }


        for(int i=0; i<n-2; i++){
            for(int j=0; j<n-2; j++){
                int coin = 0;
                coin = checkCoin(arr, i, j);
                maxCoin = Math.max(maxCoin, coin);
            }
        }

        System.out.println(maxCoin);





        // 여기에 코드를 작성해주세요.
    }
}