import java.util.*;

public class Main {

    public static int[] dx = new int[]{1,0,-1,0};
    public static int[] dy = new int[]{0,-1,0,1};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int x = 0;
        int y = 0;
        int dir = 3;

        String a = sc.next();


        for(int i=0; i<a.length(); i++){
            int n = a.charAt(i);

            if(n == 'L'){
                dir = (dir - 1 + 4) %4;

            }else if(n == 'R'){
                dir = (dir + 1)%4;

            }else if(n == 'F'){
                x+= dx[dir];
                y+= dy[dir];
            }
        }

        System.out.println(x + " " + y);
        // 여기에 코드를 작성해주세요.
    }
}