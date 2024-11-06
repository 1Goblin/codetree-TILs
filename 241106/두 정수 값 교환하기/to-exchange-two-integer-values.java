import java.util.Scanner;

class IntWrapper{
    int value;

    public IntWrapper(int value){
        this.value = value;
    }
}


public class Main {

    public static void swap(IntWrapper a, IntWrapper b){
        int temp;

        temp = a.value;
        a.value = b.value;
        b.value = temp;

    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();

        IntWrapper ai = new IntWrapper(a);
        IntWrapper bi = new IntWrapper(b);

        swap(ai,bi);

        System.out.println(ai.value + " "+ bi.value);
        // 여기에 코드를 작성해주세요.
    }
}