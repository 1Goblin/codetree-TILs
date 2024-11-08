import java.util.*;

class Student implements Comparable<Student>{
    String name;
    Integer korea;
    Integer english;
    Integer math;

    public Student(String name, Integer korea, Integer english, Integer math) {
        this.name = name;
        this.korea = korea;
        this.english = english;
        this.math = math;
    }

    @Override
    public int compareTo(Student student){
        return (this.korea+this.english+this.math) - (student.korea+student.english+student.math);
    }
}

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        Student[] students = new Student[n];



        for (int i = 0; i < n; i++) {
            String name = sc.next();
            Integer korea = sc.nextInt();
            Integer english = sc.nextInt();
            Integer math = sc.nextInt();
            students[i] = (new Student(name, korea, english, math));
        }

        Arrays.sort(students);

        for (Student student : students) {
            System.out.println(student.name + " "
                    + student.korea + " "
                    + student.english + " "
                    + student.math);
        }

        // 여기에 코드를 작성해주세요.
    }
}