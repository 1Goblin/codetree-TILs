import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String a = sc.next();
        int len = a.length();

        String ans = a.substring(0,1) + "a" + a.substring(2,len-2) + "a" + a.substring(len-1,len);
        // 여기에 코드를 작성해주세요.
        System.out.println(ans);
    }
}