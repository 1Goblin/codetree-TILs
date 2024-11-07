class a{
    String code;
    String point;
    Integer time;

    public a(String code, String point, Integer time){
        this.code = code;
        this.point = point;
        this.time = time;
    }

}

public class Main {
    public static void main(String[] args) {

        a codetree = new a("codetree", "L", 13);
        System.out.println("secret code : " + codetree.code);
        System.out.println("meeting point : " + codetree.point);
        System.out.println("time : " + codetree.time);
        // 여기에 코드를 작성해주세요.
    }
}