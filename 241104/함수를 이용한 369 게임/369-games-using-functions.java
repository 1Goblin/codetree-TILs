import java.util.Scanner;

public class Main {

    public static boolean has369(int n){
        int ans = n;

        while(true){
            
            if((ans%10) != 0 && (ans%10) %3 ==0){
                return true;
            }

            if(ans/10 == 0){
                return false;
            }
            ans = ans/10;

        }

    }

    public static boolean mul3(int n){
        return n%3==0;
    }

    public static int answerNum(int a,int b){
        int ans = 0;
        for(int i=a; i<=b; i++){
            if(has369(i) || mul3(i)){
                ans++;
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        System.out.println(answerNum(a,b));
        // 여기에 코드를 작성해주세요.
    }
}