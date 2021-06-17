package hello.hellospring.domain;

import javax.persistence.*;

@Entity // jpa 가 관리하는 entity
public class Member {

    @Id @GeneratedValue(strategy = GenerationType.IDENTITY) // identity 란 디비가 네임만 넣어도 아이디를 알아서 생성
    private Long id;

    private String name;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
