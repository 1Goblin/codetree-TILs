import java.util.Scanner;

public class Main {

    public static boolean isYun(int year){
        
        if(year%100 ==0 && year%400 != 0){
            return false;
        }

        if(year%4==0){
            return true;
        }


        return false;

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int year = sc.nextInt();

        if(isYun(year)){
            System.out.println("true");
        }else{
            System.out.println("false");
        }
        // 여기에 코드를 작성해주세요.
    }
}