package dnlxo.dnlxospring.service;

import dnlxo.dnlxospring.domain.Member;
import dnlxo.dnlxospring.repository.MemberRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class MemberService {

    private final MemberRepository memberRepository;

    @Autowired
    public MemberService(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }

    public String join(Member member) {

        validateDuplicateMember(member);
        memberRepository.save(member);
        return member.getId();
    }

    private void validateDuplicateMember(Member member) {
        memberRepository.findById(member.getId())
                .ifPresent(m -> { // 그니까 null값이 아니면 즉 멤버가 이미 레포에 있으니까
                    throw new IllegalStateException("이미 존재하는 회원입니다.");
                });
    }
}
