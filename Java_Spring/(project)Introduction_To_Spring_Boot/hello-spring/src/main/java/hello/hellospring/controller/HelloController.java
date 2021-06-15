package hello.hellospring.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class HelloController {

    @GetMapping("hello")
    public String hello(Model model) {
        model.addAttribute("data", "hello!!");
        return "hello";
    }

    @GetMapping("hello-mvc")
    public String helloMvc(@RequestParam("name") String name, Model model) { //requestparam 안에있는 초록색 name 이 파라미터 받는 거
        model.addAttribute("name", name); // ?name=~~~ 하면 하얀색 String name 이 ~~~가 되고.
        return "hello-template";
    }

    @GetMapping("hello-string")
    @ResponseBody //이걸 http 통신 프로토콜에서 응답 바디부에 직접 넣겠다. html바디 부가 아님
    public String helloString(@RequestParam("name") String name) {
        return "hello " + name; // 템플릿 엔진과의 차이점은 뷰 이런게 없고 이 문자가 그대로 내려간다.
        // 페이지 소스를 보아도 html 파일 코드가 없고 그냥 무식하게 저 문자만 나온다 hello 어쩌고.
    }

    // 데이터를 내놔! 하면...
    @GetMapping("hello-api")
    @ResponseBody // 리스폰스바디하면 기본으로 json 반환
    public Hello helloApi(@RequestParam("name") String name) {
        Hello hello = new Hello();
        hello.setName(name);
        return hello;
    }

    static class Hello {
        private String name;

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }
    } // json 이라는 방식으로 내려준다.
}
