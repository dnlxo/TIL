package dnlxo.dnlxospring.controller;

import dnlxo.dnlxospring.domain.Member;
import dnlxo.dnlxospring.service.MemberService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

@Controller
public class MemberController {

    private final MemberService memberService;

    @Autowired
    public MemberController(MemberService memberService) {
        this.memberService = memberService;
    }

    @GetMapping("/members/new")
    public String createForm() {
        return "memberInsertForm";
    }

    @PostMapping("/members/new")
    public String create(MemberForm form) {
        Member member = new Member();
        member.setName(form.getName());
        member.setId(form.getId());
        member.setPw(form.getPw());

        System.out.println("name :" + member.getName());
        System.out.println("id :" + member.getId());
        System.out.println("pw :" + member.getPw());
        System.out.println("비밀번호 확인 :" + form.getPwCheck());

        memberService.join(member);
        return "redirect:/";


    }
}
