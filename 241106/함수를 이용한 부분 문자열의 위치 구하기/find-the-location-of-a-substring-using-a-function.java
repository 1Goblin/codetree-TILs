import java.util.Scanner;

public class Main {
    public static int test(String a, String b){

        for(int i=0; i<a.length(); i++){
            for(int j=0; j<b.length(); j++){
                if(a.charAt(i+j) != b.charAt(j)){
                    break;
                }

                if(j==b.length()-1){
                    return i;
                }
            }
        }

        return -1;
    }
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        String a = sc.next();
        String b = sc.next();

        System.out.println(test(a,b));

        // 여기에 코드를 작성해주세요.
    }
}