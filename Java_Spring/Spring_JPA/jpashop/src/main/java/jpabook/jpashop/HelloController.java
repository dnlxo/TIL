package jpabook.jpashop;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HelloController {

    @GetMapping("hello")
    public String hello(Model model) {
        model.addAttribute("data", "hello!!"); // 데이터를 뷰에 넘긴다.
        return "hello"; // 리소스에 템플릿에 hello.html 이 잇으면 글로 보냄 (설정이 글케 되어잇음)
    }
}