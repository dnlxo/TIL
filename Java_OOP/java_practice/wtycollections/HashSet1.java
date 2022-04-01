import java.util.HashSet;

public class HashSet1 {

    public static void main(String[] args) {
        HashSet<Integer> A = new HashSet<Integer>();
        A.add(1);
        A.add(2);
        A.add(2);
        System.out.println(A);
        // A.addAll(B); 합집합
        // A.retainAll(B); 교집합
        // A.removeAll(B); 차집합
        // HashSet 은 순서가 보장되지 않고, 중복이 안된다.
    }
}