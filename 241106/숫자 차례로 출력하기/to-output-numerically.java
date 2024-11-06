import java.util.Scanner;

public class Main {

    public static void ftn(int n){
        if(n==0){
            return;
        }


        System.out.printf("%d ", n);

        ftn(n-1);

    }

    public static void ntf(int n){
        if(n==0){
            return;
        }

        ntf(n-1);

        System.out.printf("%d ", n);

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        ntf(n);
        System.out.println();
        ftn(n);
        // 여기에 코드를 작성해주세요.
    }
}