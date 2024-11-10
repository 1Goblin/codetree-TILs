import java.util.*;

public class Main {
    public static void paintSq(int[][] arr, int x1, int x2, int y1, int y2){
        for(int i=x1; i<y1; i++){
            for(int j=x2; j<y2; j++){
                arr[i][j] +=1;
            }
        }
    }
    public static void paintSqM(int[][] arr, int x1, int x2, int y1, int y2){
        for(int i=x1; i<y1; i++){
            for(int j=x2; j<y2; j++){
                arr[i][j] -=1;
            }
        }
    }

    public static int showArea(int[][] arr){

        int area = 0;

        for(int i=0; i<2000; i++){
            for(int j=0; j<2000; j++){
                if(arr[i][j] == 1){
                    area+=1;
                }
            }
        }

        return area;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[][] arr = new int[2000][2000];

        for(int i=0; i<2; i++){
            int x1 = sc.nextInt()+1000;
            int x2 = sc.nextInt()+1000;
            int y1 = sc.nextInt()+1000;
            int y2 = sc.nextInt()+1000;

            paintSq(arr, x1, x2, y1, y2);
        }

        int x1 = sc.nextInt()+1000;
        int x2 = sc.nextInt()+1000;
        int y1 = sc.nextInt()+1000;
        int y2 = sc.nextInt()+1000;

        paintSqM(arr, x1, x2, y1, y2);


        System.out.println(showArea(arr));



        // 여기에 코드를 작성해주세요.
    }
}