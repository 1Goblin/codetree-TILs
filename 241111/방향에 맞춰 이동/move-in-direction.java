import java.util.*;

public class Main {
    public static int[] dx = new int[]{0,0, -1, 1};
    public static int[] dy = new int[]{1,-1,0,0};

    public static int[][] arr = new int[100][100];


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int nx = 0;
        int ny = 0;

        for(int i=0; i<n; i++){
            char dir = sc.next().charAt(0);
            int dis = sc.nextInt();


            if(dir == 'N'){
                nx+= dx[0] * dis;
                ny+= dy[0] * dis;

            }else if(dir == 'E'){
                nx+= dx[3] * dis;
                ny+= dy[3] * dis;

            }else if(dir == 'S'){
                nx+= dx[1] * dis;
                ny+= dy[1] * dis;

            }else if(dir == 'W'){
                nx+= dx[2] * dis;
                ny+= dy[2] * dis;
            }
        }
        System.out.println(nx + " " + ny);


        // 여기에 코드를 작성해주세요.
    }
}