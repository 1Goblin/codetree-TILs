import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int sum = 0;
        int sum2 = 0;
        int cnt = 0;
        int[] arr = new int[10];

        for(int i=0; i<10; i++){
            arr[i] = sc.nextInt();
        }

        for(int i=1; i<10; i++){
            if(i%2==1){
                sum+=arr[i];
            }
            
            if((i+1)%3==0){
                sum2+=arr[i];
                cnt++;
            }
        }


        double avg = (double)sum2/cnt;

        System.out.printf("%d %.1f",sum, avg);
        // 여기에 코드를 작성해주세요.
    }
}