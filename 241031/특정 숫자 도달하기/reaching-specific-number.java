import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int sum = 0;
        double ans = 0.0;

        int[] arr = new int[10];

        for(int i=0; i<10; i++){
            arr[i] = sc.nextInt();
        }


        for(int i=0; i<10; i++){
            if(arr[i]>=250){
                break;
            }
            sum+=arr[i];
            ans = (double)sum / (i+1);
        }
        

        System.out.printf("%d %.1f", sum, ans);
        

    }
}