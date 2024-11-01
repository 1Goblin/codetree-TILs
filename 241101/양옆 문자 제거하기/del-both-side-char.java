import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String a = sc.next();

        int len = a.length();
        a = a.substring(0,1)+a.substring(2,len-2)+a.substring(len-1,len);
        System.out.println(a);
        // 여기에 코드를 작성해주세요.
    }
}