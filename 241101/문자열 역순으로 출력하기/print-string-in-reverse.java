import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = 4;
        String[] arr = new String[4];

        for(int i=0; i<n; i++){
            arr[i] = sc.next();
        }

        for(int i=3; i>-1; i--){
            System.out.println(arr[i]);
        }

        // 여기에 코드를 작성해주세요.
    }
}