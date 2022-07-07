package hello.servlet.basic;

import lombok.Getter;
import lombok.Setter;

// json 형식으로 파싱하기 위해서 객체를 생성한 것
@Getter @Setter
public class HelloData {

    private String username;
    private int age;

}