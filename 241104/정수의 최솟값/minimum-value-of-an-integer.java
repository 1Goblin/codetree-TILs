import java.util.Scanner;

public class Main {

    public static int printAs(int a, int b, int c){
        if(a>=b){
            if(b>=c){
                return c;
            }
            else{
                return b;
            }
        }else{
            if(a>=c){
                return c;
            }
            else{
                return a;
            }
        }
    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        System.out.println(printAs(a,b,c));

        // 여기에 코드를 작성해주세요.
    }
}