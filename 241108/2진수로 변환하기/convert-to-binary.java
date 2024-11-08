import java.util.Scanner;

public class Main {

    public static int[] makeBinary(int n){

        int[] binary = new int[20];
        int cnt = 0;

        while(true){
            if(n < 2){
                binary[cnt++] = n;
                break;
            }
            
            binary[cnt++] = n%2;
            n = n/2;
        }

        int[] result = new int[cnt];

        for(int i=0; i<cnt; i++){
            result[i] = binary[i];
        }

        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] binary = makeBinary(n);

        for(int i=binary.length -1 ; i>=0; i--){
            System.out.print(binary[i]);

        }

        // 여기에 코드를 작성해주세요.
    }
}