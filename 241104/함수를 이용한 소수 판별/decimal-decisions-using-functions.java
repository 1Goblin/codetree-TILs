import java.util.Scanner;

public class Main {

    public static boolean isPrime(int n){
        for(int i=2; i<n; i++){
            if(n%i==0){
                return false;
            }
        }
        return true;
        
    }

    public static int primeSum(int a, int b){
        int primeSum = 0;
        for(int i=a; i<=b; i++){
            if(isPrime(i)){
                primeSum+=i;
            }
        }

        return primeSum;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();

        System.out.println(primeSum(a,b));
        // 여기에 코드를 작성해주세요.
    }
}