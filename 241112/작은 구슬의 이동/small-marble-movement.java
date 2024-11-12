import java.util.*;

public class Main {
    
    public static int[] dx = new int[]{0,0,-1,1};
    public static int[] dy = new int[]{1,-1,0,0};
    public static int n;
    public static int t;

    public static int inputDir(char a){

        if(a == 'U'){
            return 2;

        }else if(a == 'D'){
            return 3;

        }else if(a == 'R'){
            return 0;

        }else{
            return 1;
        }
    }

    public static boolean inRange(int x, int y){
        return (x >0 && y >0 && x<= n && y <= n);
    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        t = sc.nextInt();

        int x = sc.nextInt();
        int y = sc.nextInt();

        char d = sc.next().charAt(0);

        int dirNum = inputDir(d);
   
        for(int i=0; i<t; i++){
            int ndx = x + dx[dirNum]; 
            int ndy = y + dy[dirNum]; 
            if(!inRange(ndx, ndy)){
                dirNum = (1-dirNum + 4)%4;

            }else{
                x+= dx[dirNum];
                y+= dy[dirNum];
            }
        }

        System.out.println((x) + " " + (y));
        // 여기에 코드를 작성해주세요.
    }
}