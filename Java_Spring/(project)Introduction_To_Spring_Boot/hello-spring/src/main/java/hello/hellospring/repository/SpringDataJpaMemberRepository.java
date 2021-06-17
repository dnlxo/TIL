package hello.hellospring.repository;

import hello.hellospring.domain.Member;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface SpringDataJpaMemberRepository extends JpaRepository<Member, Long>, MemberRepository {
// Spring JPA 가 인터페이스를 보면 자동으로 구현체를 만들어서 빈에 등록해준다.
    @Override
    Optional<Member> findByName(String name);
}
