import java.util.*;

class Student{
    String name;
    Integer height;
    Integer weight;

    public Student(String name, Integer height, Integer weight){
        this.name = name;
        this.height = height;
        this.weight = weight;
    }

    public int getHeight(){
        return this.height;
    }

}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        List<Student> students = new ArrayList<>();

        for(int i=0; i<n; i++){
            String name = sc.next();
            Integer height = sc.nextInt();
            Integer weight = sc.nextInt();
            
            students.add(new Student(name, height, weight));
        }

        students.sort(Comparator.comparingInt(Student::getHeight));

        for(int i=0; i<n; i++){
            System.out.println(students.get(i).name + " " +students.get(i).height + " " +students.get(i).weight + " ");
        }

        // 여기에 코드를 작성해주세요.
    }
}