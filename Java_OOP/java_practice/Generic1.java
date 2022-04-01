class EmployeeInfo {
    public int rank;
    EmployeeInfo(int rank) {
        this.rank = rank;
    }
}
class Person<T, S> { // T extends ~~  붙이면 제네릭 제한 가능
    public T info;
    public S id;
    Person(T info, S id) {
        this.info = info;
        this.id = id;
    }
}

public class Generic1 {
    // 제네릭이란? 클래스 내부에서 사용할 데이터 타입을 외부에서 지정하는 기법.
    
    public static void main(String[] args) {
        EmployeeInfo e = new EmployeeInfo(1);
        Integer i = 10;
        // Person<EmployeeInfo, Integer> p1 = new Person<EmployeeInfo, Integer>(e, i);
        // 위와 같은 경우 e와 i가 어떤 타입인지 알고있기 때문에
        Person p1 = new Person(e, i);
        // 라고 써도 된다.
    }
}

