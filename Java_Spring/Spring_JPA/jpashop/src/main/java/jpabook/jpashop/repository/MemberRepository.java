package jpabook.jpashop.repository;

import jpabook.jpashop.domain.Member;
import org.springframework.stereotype.Repository;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import java.util.List;

@Repository // 컴포넌트 스캔에 의해 자동으로 스프링 빈으로 관리가 된다.
public class MemberRepository { // 리포지토리? 엔티티같은걸 찾아주는 애

    @PersistenceContext
    private EntityManager em;

    public void save(Member member) {
        em.persist(member); // jpa가 저장하는 로직
    }

    public Member findOne(Long id) {
        return em.find(Member.class, id); // jpa가 멤버를 찾아서 반환해준다.
    }

    public List<Member> findAll() {
        return em.createQuery("select m from Member m", Member.class)
                .getResultList(); // (jpql 작성, 반환타입) sql이랑 다른점?
                                // 거의같은데 from의 대상이 테이블대상 쿼리가아니고 엔티티 대상 쿼리
    }

    public List<Member> findByName(String name) {
        return em.createQuery("select m from Member m where m.name = :name", Member.class)
                .setParameter("name", name)
                .getResultList();
    }

}
