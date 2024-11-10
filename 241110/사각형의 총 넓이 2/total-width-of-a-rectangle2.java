import java.util.*;

public class Main {
    public static void paintSq(int[][] arr, int x1,int y1,int x2,int y2){

        for(int i=x1; i<x2; i++){
            for(int j=y1; j<y2; j++){
                arr[i][j] += 1;
            }
        }
    }

    public static int sqArea(int[][] arr){
        int area = 0;

        for(int i=0; i<200; i++){
            for(int j=0; j<200; j++){
                if(arr[i][j] > 0){
                    area+=1;
                }
            }
        }

        return area;

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int arr[][] = new int[200][200];

        for(int i=0; i<n; i++){
            int x1 = sc.nextInt()+100;
            int x2 = sc.nextInt()+100;
            int y1 = sc.nextInt()+100;
            int y2 = sc.nextInt()+100;

            paintSq(arr,x1,x2,y1,y2);
        }

        System.out.println(sqArea(arr));
        // 여기에 코드를 작성해주세요.
    }
}