package hello.hellospring.service;

import hello.hellospring.domain.Member;
import hello.hellospring.repository.JdbcMemberRepository;
import hello.hellospring.repository.MemberRepository;
import hello.hellospring.repository.MemoryMemberRepository;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.transaction.annotation.Transactional;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.assertThrows;

@SpringBootTest
@Transactional // db 의 트렌젝션. 오토커밋 노노 커밋하기전까진 실제디비에 반영안되는것. 걍 롤백해버림 그래서 에프터이치 그런거 할 필요없음.(테스트에 붙엇을때만)
class MemberServiceIntegrationTest {

    @Autowired MemberService memberService;
    @Autowired MemberRepository memberRepository;

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