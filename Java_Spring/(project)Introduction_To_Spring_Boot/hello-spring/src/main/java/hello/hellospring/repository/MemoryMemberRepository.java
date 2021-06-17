package hello.hellospring.repository;

import hello.hellospring.domain.Member;
import org.springframework.stereotype.Repository;

import java.util.*;

//@Repository
//동작하는지 확인하고 싶다. 테스트 케이스를 작성하면 댄다.
public class MemoryMemberRepository implements MemberRepository {

    private static Map<Long, Member> store = new HashMap<>(); // 키와 값
    private static long sequence = 0L; // 키값 생성해주는 애

    @Override
    public Member save(Member member) {
        member.setId(++sequence); // id 값 세팅
        store.put(member.getId(), member);
        return member;
    }

    @Override
    public Optional<Member> findById(Long id) {
        return Optional.ofNullable(store.get(id)); // null 처리 해야하는데 그걸 요즘은 optional로 함
    }

    @Override
    public Optional<Member> findByName(String name) {
        return store.values().stream()
                .filter(member -> member.getName().equals(name))
                .findAny();
    }

    @Override
    public List<Member> findAll() { // Map 인데 반환은 list 실무에서 많이 씀
        return new ArrayList<>(store.values());
    }

    public void clearStore() {
        store.clear();
    }
}
