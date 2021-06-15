package hello.hellospring.service;

import hello.hellospring.domain.Member;
import hello.hellospring.repository.MemoryMemberRepository;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.*;
import static org.junit.jupiter.api.Assertions.*;

class MemberServiceTest {

//  MemberService memberService = new MemberService();
//  MemoryMemberRepository memberRepository = new MemoryMemberRepository(); // << 이놈의 문제점? 실제 Memberservice 에있는
    // 메모리 멤버 리포지토리랑 서로 다른 놈이다 새로운 인스턴스. 같은걸로 테스트 되는게 좋다. 중요
    // 멤버 서비스에서 멤버리포지토리 new 지우고 생성
    // 그리고 before each
    MemberService memberService;
    MemoryMemberRepository memberRepository;

    @BeforeEach // 각 테스트 실행 전에
    public void beforeEach() {
        memberRepository = new MemoryMemberRepository();
        memberService = new MemberService(memberRepository);
    }

    @AfterEach
    public void afterEach() {
        memberRepository.clearStore();
    }
    // 테스트 할때 값 누적이 되는 것 항상 클리어 해줘야함

    @Test
    void 회원가입() {
        //given
        Member member = new Member();
        member.setName("spring");

        //when
        Long saveId = memberService.join(member); // join은 레포에 저장하고 그 회원의 아이디를 리턴하도록 되어있음.
        // 중복 되어서 가입안되었으면 null 값이려나 ?

        //then
        Member findMember = memberService.findOne(saveId).get();
        assertThat(member.getName()).isEqualTo(findMember.getName());
    }

    @Test
    public void 중복_회원_예외() {
        //given
        Member member1 = new Member();
        member1.setName("spring");

        Member member2 = new Member();
        member2.setName("spring");

        //when
        memberService.join(member1);
        /** try catch 문 대신에 */
        assertThrows(IllegalStateException.class, () -> memberService.join(member2)); // 람다식 로직을 태울 때 저 익셉션이 터져야함
        // 성공하면 테스트 통과. // 다른 일리걸 스테이트 대신에 다른 익셉션이라고하면 통과실패
        // assertThrows 는 반환도 가능함
        IllegalStateException e = assertThrows(IllegalStateException.class, () -> memberService.join(member2));

        assertThat(e.getMessage()).isEqualTo("이미 존재하는 회원입니다.");

//        try {
//            memberService.join(member2);
//            fail();
//        } catch (IllegalStateException e) {
//            // 일로 와야 예외가 정상적으로 터진거임
//            assertThat(e.getMessage()).isEqualTo("이미 존재하는 회원입니다.");
//        }

        //then
    }

    @Test
    void findMembers() {
    }

    @Test
    void findOne() {
    }
}