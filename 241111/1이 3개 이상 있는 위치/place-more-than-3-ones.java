import java.util.*;

public class Main {

    public static int[] dx = new int[]{1,-1,0,0};
    public static int[] dy = new int[]{0,0,1,-1};
    public static int n;


    public static boolean inRange(int x, int y){
        return (0 <= x && n > x && 0 <= y && n > y);
    }

    public static int adjNum(int[][] arr, int x, int y){
        int cnt = 0;

        for(int dir=0; dir<4; dir++){
            int nx = x + dx[dir];
            int ny = y + dy[dir];
            if(inRange(nx, ny) && arr[nx][ny] == 1){
                cnt++;
            }
        }

        return cnt;

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();

        int[][] arr = new int[n][n];
        int ans = 0;

        int x = 0;
        int y = 0;

        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                arr[i][j] = sc.nextInt();
            }
        }

        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(adjNum(arr, i, j) > 2){
                    ans+=1;
                }

            }
        }
        System.out.println(ans);

        // 여기에 코드를 작성해주세요.
    }
}