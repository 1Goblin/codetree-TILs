import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        char n = sc.next().charAt(0);

        char[] arr = new char[]{'L','E','B','R','O','S'};

        int ans = -1;

        for(int i=0; i<6; i++){
            if(arr[i] == n){
                ans = i;
            }
        }

        if(ans == -1){
            System.out.println("None");
        }else{
            System.out.println(ans);
        }

        // 여기에 코드를 작성해주세요.
    }
}