import java.util.*;

public class Main {
    public static int minCal(int b, int d){
        return d-b;
    }

    public static int hourCal(int a, int c){

        return (c-a)*60;
    }

    public static int timeCal(int a, int b, int c, int d){

        return hourCal(a,c) + minCal(b,d);
    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int d = sc.nextInt();

        int ans = 0;
        


        ans = timeCal(a,b,c,d);

        System.out.println(ans);


        // 여기에 코드를 작성해주세요.
    }
}