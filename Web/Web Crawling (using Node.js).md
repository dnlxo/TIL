## ⚡️ Web Crawling (using Node.js)

---

### 웹 크롤링

- 웹 상에 있는 데이터들을 가져와서 저장하려고 할 때, 혹은 특정 홈페이지에 있는 가격정보나 날씨 정보를 가져오려고 할 때 특별한 API가 제공되지 않거나 혹은 제약이 심할 때 사용할 수 있는 방법
- 외국에선 'Web Crawling' 보다는 'Web Scraping' 이라는 용어를 자주 사용
- HTML의 소스들의 **규칙을 분석**해서 우리가 **원하는 정보들만 뽑아오는 것**

---

### axios

- Axios는 브라우저, Node.js를 위한 Promise API를 활용하는 HTTP 비동기 통신 라이브러리입니다.
- 특징
  - 운영 환경에 따라 브라우저의 XMLHttpRequest 객체 또는 Node.js의 http api 사용
  - Promise(ES6) API 사용
  - 요청과 응답 데이터의 변형
  - HTTP 요청 취소
  - HTTP 요청과 응답을 JSON 형태로 자동 변경

---

### cheerio

- 서버를 위해 특별히 설계된 빠르고 유연한 핵심 jQuery이다.
- node.js로 받아온 웹 페이지를 조작할 수 있게 도와주는 라이브러리
- 기본적으로 jQuery를 사용해 DOM에 접근
- 데이터 파싱 및 추출이 매우 쉬워진다.

---

### 출처

- https://m.blog.naver.com/potter777777/220605598446
- https://velog.io/@zofqofhtltm8015/Axios-%EC%82%AC%EC%9A%A9%EB%B2%95-%EC%84%9C%EB%B2%84-%ED%86%B5%EC%8B%A0-%ED%95%B4%EB%B3%B4%EA%B8%B0
- https://kyun2da.dev/%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC/axios-%EA%B0%9C%EB%85%90-%EC%A0%95%EB%A6%AC/
- https://joshua1988.github.io/vue-camp/vue/axios.html
- https://github.com/sooojungee/TIL/blob/master/vue/180918.%5BVue%5D%20cheerio.md
