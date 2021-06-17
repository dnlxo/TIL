package hello.hellospring.controller;

import hello.hellospring.domain.Member;
import hello.hellospring.repository.MemberRepository;
import hello.hellospring.service.MemberService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import java.util.List;

@Controller // 스프링 컨테이너가 이 어노테이션을 보면 멤버컨트롤러 라는 객체를 생성해서 넣어두고 스프링이 관리
// 이것을 스프링 컨테이너에서 스프링 빈이 관리된다고 한다.
public class MemberController {

//  private final MemberService memberService = new MemberService(); // 여러개 생성할 필요가 없다.
    // 이제 스프링 컨테이너에 등록하고 하나만 쓴다.

    private final MemberService memberService;
    // 스프링 빈으로 등록되어야 오토와이어드가 동작 함.
    @Autowired // 스프링 컨테이너가 이 객체 생성! 그럴때 생성자가 호출 된다. 근데 이 오토와이어드가 붙어있으면 멤버서비스를 스프링이
    // 스프링 컨테이너에 있는 멤버서비스를 가져다가 연결 시켜준다. >> 서비스에 가서 @서비스 붙여줘야댐
    public MemberController(MemberService memberService) {
        this.memberService = memberService;
    }

    @GetMapping("/members/new")
    public String createForm() {
        return "members/createMemberForm"; // 템플릿에서 해당파일 찾아서 뿌림 근데 그때 그 파일안에 폼이라는 태그가 있으면,
    }

    @PostMapping("/members/new") // 데이터를 폼같은곳에 넣어서 전달할 때 포스트. 주소는 똑같지만 방식에 따라 다르게 매핑할수잇다.
    public String create(MemberForm form) { // 멤버 폼이라는 객체는 이름을 가지고잇따.
        Member member = new Member(); // 새로운 멤버객체를 만들고 (아이디와 네임을 가지고잇다.)
        member.setName(form.getName()); // 폼에서 받아온 네임으로 멤버 네임을 설정한다.

        memberService.join(member);

        return "redirect:/";
    }

    @GetMapping("/members")
    public String list(Model model) {
        List<Member> members = memberService.findMembers();
        model.addAttribute("members", members);
        return "members/memberList";
    }
}
