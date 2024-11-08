import java.util.*;

class Student {
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

    public String getName() {
        return this.name;
    }

    public Integer getKorea() {
        return this.korea;
    }

    public Integer getEnglish() {
        return this.english;
    }

    public Integer getMath() {
        return this.math;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        List<Student> students = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            String name = sc.next();
            Integer korea = sc.nextInt();
            Integer english = sc.nextInt();
            Integer math = sc.nextInt();
            students.add(new Student(name, korea, english, math));
        }

        // 국어 점수 내림차순, 영어 점수 오름차순, 수학 점수 내림차순
        students.sort(Comparator.comparingInt(Student::getKorea).reversed()
                .thenComparing(Comparator.comparingInt(Student::getEnglish).reversed())
                .thenComparing(Comparator.comparingInt(Student::getMath).reversed()));

        for (Student student : students) {
            System.out.println(student.getName() + " "
                    + student.getKorea() + " "
                    + student.getEnglish() + " "
                    + student.getMath());
        }
    }
}