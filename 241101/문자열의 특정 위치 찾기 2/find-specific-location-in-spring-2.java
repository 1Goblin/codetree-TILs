import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char a = sc.next().charAt(0);
        int cnt = 0;

        String[] arr = new String[]{"apple", "banana", "grape", "blueberry", "orange"};

        for(int i=0; i<arr.length; i++){
            String str = arr[i];
            for(int j =2; j<4; j++){
                if(a == str.charAt(j)){
                    System.out.println(arr[i]);
                    cnt++;
                    break;
                }
            }
        }
        System.out.println(cnt);
        // 여기에 코드를 작성해주세요.
    }
}