## 1_HTML5 기본 용어

- 태그와 요소

  - HTML 페이지를 구성하는 각 부품을 요소라고 한다.

  - 요소를 만들 때 사용하는 작성방법 : 태그

  - 태그와 요소라는 단어를 구분하지 않고 사용한다.

  - ```html
    <h1>
        내용
    </h1>
    
    <img>
    <br>
    <hr>
    <!-- 내용이 있는 요소와 없는 요소들... -->
    ```

- 속성

  - 태그에 추가 정보를 부여할 때 사용

  - ```html
    <img src = "image.png">
    ```

----

## HTML5 페이지의 구조

```html
<!DOCTYPE html> <!-- 웹 브라우저에 HTML5 문서라는 것을 알리기 위함-->
<html>
<head>
</head> <!-- 바디 태그에 필요한 css, js를 제공-->
<body>

</body> <!-- 사용자에게 실제로 보이는 부분 작성-->
    
</html> <!-- 모든 태그는 html 태그 내부에 작성-->
```

---

## CSS와 JS

```html
<!-- CSS -->
<head>
    <style>
        여기에 작성
    </style>
</head>

또는 외부에 .css 파일로 작성 후
<head>
    <link rel = "stylesheet" href = "Style.css">
</head>
<body>
    <h1>
        여기 내용을 스타일
    </h1>
</body>

<!-- JS -->
헤드 내부에 <script> 여기에 js 작성</script>

또는 외부에 .js 파일로 작성 후
헤드 내부 <script src = ".js"></script>
```

- 외부 스타일시트는 link
- 외부 자바스크립트는 script

---





