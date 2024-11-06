import java.util.Scanner;

public class Main {
    public static void printString(int n){
        if(n==0){
            return;
        }
        System.out.println("HelloWorld");

        printString(n-1);

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        printString(n);

        // 여기에 코드를 작성해주세요.
    }
}