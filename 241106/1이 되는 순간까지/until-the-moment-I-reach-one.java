import java.util.Scanner;

public class Main {

    public static int printAns(int n){

        if(n==1){
            return 0;
        }

        if(n%2==0){
            return printAns(n/2) + 1;

        }else{
            return printAns(n/3) + 1;
        }
        

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        printAns(n);

        System.out.println(printAns(n));
        // 여기에 코드를 작성해주세요.
    }
}