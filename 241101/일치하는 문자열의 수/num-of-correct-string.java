import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        String a = sc.next();

        int ans = 0;

        for(int i=0; i<n; i++){
            String t = sc.next();
            if(t.equals(a)){
                ans++;
            }
        }

        System.out.println(ans);

        // 여기에 코드를 작성해주세요.
    }
}