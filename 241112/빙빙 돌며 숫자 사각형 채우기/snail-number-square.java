import java.util.*;

public class Main {

    public static int n;
    public static int m;
    public static int[] dx = {0, 1,  0, -1};
    public static int[] dy = {1, 0, -1,  0};

    public static boolean isRange(int x, int y){
        return (x>=0 && y>=0 && x<n && y<m);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        m = sc.nextInt();

        int[][] arr = new int[n][m];

        int x = 0;
        int y = 0;

        int dir = 0;

        arr[x][y] = 1;


        for(int i=2; i<=n*m; i++){
            int ndx = x + dx[dir]; 
            int ndy = y + dy[dir];

            if(!isRange(ndx, ndy) || arr[ndx][ndy] != 0){
                dir = (dir + 1) % 4;
            }
            
            x += dx[dir];
            y += dy[dir];

            arr[x][y] = i;
            
        }



        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                System.out.printf("%d ", arr[i][j]);
            }
            System.out.println();
        }


    }
}