import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String a = sc.next();

        int num = 0;

        for(int i=0; i<a.length(); i++){
            
            num = num * 2 + (a.charAt(i) - '0');
        }

        System.out.println(num);

        

        
        // 여기에 코드를 작성해주세요.
    }
}