import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 문자열을 정의합니다.
        String a;
        String b;
        String str1;
        String str2;
        
        // 문자열을 입력받습니다.
        a = sc.next();
        b = sc.next();

        str1 = a+b;
        str2 = b+a;

        int intA = Integer.parseInt(str1);
        int intB = Integer.parseInt(str2);

        System.out.println(intA+intB);
    }
}