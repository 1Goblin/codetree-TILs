import java.util.Scanner;

public class Main {

    public static int printAns(int n){

        if(n==1){
            return 1;
        }
        
        return printAns(n-1) + n;

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();


        System.out.println(printAns(n));

        // 여기에 코드를 작성해주세요.
    }
}