package dnlxo.dnlxospring.repository;

import dnlxo.dnlxospring.domain.Member;

import java.util.Optional;

public interface MemberRepository {
    Member save(Member member);
    Optional<Member> findById(String id);
}
