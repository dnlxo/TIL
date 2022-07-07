package hello.servlet.basic;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet(name = "helloServlet", urlPatterns = "/hello") // 이름은 아무거나 주고, /hello로 오면 밑에가 실행되는 것
public class HelloServlet extends HttpServlet { // 상속 받아야함

    @Override
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    // 서블릿이 호출되면, 이 서비스 메서드가 실행된다.
        System.out.println("HelloServlet.service");
        System.out.println("request = " + request);
        System.out.println("response = " + response);

        String username = request.getParameter("username"); // 파라미터에서 값을 꺼낼 수 있음
        System.out.println("username = " + username);

        response.setContentType("text/plain"); // 응답 정보를 설정 중
        response.setCharacterEncoding("utf-8");
        response.getWriter().write("hello " + username); // 바디에 메세지가 들어간다.
    }
}
