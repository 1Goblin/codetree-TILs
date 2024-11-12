import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String a = sc.next();

        int cnt = 0;

        for(int i=0; i<a.length(); i++){
            if(a.charAt(i) == '('){
                for(int j=i; j<a.length(); j++){
                    if(a.charAt(j) == ')'){
                        cnt++;
                    }

                }

            }
        }

        System.out.println(cnt);
        
    }
}