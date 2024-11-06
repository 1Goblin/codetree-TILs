import java.util.Scanner;

public class Main {
    public static boolean tt(String a){

        for(int i=0; i<a.length(); i++){
            if(a.charAt(i) != a.charAt(a.length()-1-i)){
                return false;
            }
        }
        return true;

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();


        if(tt(a)){
            System.out.println("Yes");
        }else{
            System.out.println("No");
        }

        // 여기에 코드를 작성해주세요.
    }
}