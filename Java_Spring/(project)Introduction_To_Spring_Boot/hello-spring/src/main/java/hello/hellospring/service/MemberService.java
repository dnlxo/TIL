package hello.hellospring.service;

import hello.hellospring.domain.Member;
import hello.hellospring.repository.MemberRepository;
import hello.hellospring.repository.MemoryMemberRepository;

import java.util.List;
import java.util.Optional;


public class MemberService {

    private final MemberRepository memberRepository;

    public MemberService(MemberRepository memberRepository) {
        this.memberRepository = memberRepository; // 직접 new 생성이 아니고 외부에서 넣어주도록 설정
    } // Dependency Injection 직접 new 하지 않고 외부에서 넣어준다.

    /**
     * 회원 가입
     */
    public Long join(Member member) {
        //같은 이름이 있는 중복 회원은 안된다.
        Optional<Member> result = memberRepository.findByName(member.getName()); // 해당 이름을 가진 멤버가 이미 레포에 있는경우
        result.ifPresent(m -> { // 그니까 null값이 아니면 즉 멤버가 이미 레포에 있으니까
            throw new IllegalStateException("이미 존재하는 회원입니다.");
        });
        // 위에 처럼 하면 길고 안이쁘다. 아래처럼 한번에 하면 댐
        validateDuplicateMember(member);
        // 근데 이것도 이니까 이런 경우에는 메소드로 뽑는게 좋다
        memberRepository.save(member);
        return member.getId();
    }

    private void validateDuplicateMember(Member member) {
        memberRepository.findByName(member.getName())
                .ifPresent(m -> { // 그니까 null값이 아니면 즉 멤버가 이미 레포에 있으니까
                    throw new IllegalStateException("이미 존재하는 회원입니다.");
                });
    }

    /**
     * 전체 회원 조회
     */
    public List<Member> findMembers() {
        return memberRepository.findAll();
    }

    public Optional<Member> findOne(Long memberId) {
        return memberRepository.findById(memberId);
    }
}

/** 이제 회원 서비스를 테스트해보자 */