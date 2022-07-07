package hello.servlet.basic.response;

import com.fasterxml.jackson.databind.ObjectMapper;

import hello.servlet.basic.HelloData;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import java.io.IOException;

/**
 * http://localhost:8080/response-json
 *
 */
@WebServlet(name = "responseJsonServlet", urlPatterns = "/response-json")
public class ResponseJsonServlet extends HttpServlet {

    private ObjectMapper objectMapper = new ObjectMapper();

    @Override
    protected void service(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        //Content-Type: application/json
        response.setHeader("content-type", "application/json");
        response.setCharacterEncoding("utf-8"); // 타입 잡기

        HelloData data = new HelloData();

        data.setUsername("kim");
        data.setAge(20);

        //{"username":"kim","age":20}
        // 객체에 먼저 저장하고,

        String result = objectMapper.writeValueAsString(data); // 객체를 json 형식으로 변환
        response.getWriter().write(result); // 최종 데이터 작성
    }
}
