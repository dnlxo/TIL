## 오라클 유틸리티 사용법

오라클의 핵심 유틸리티

- SQL Developer
- SQL*Plus
- Application Express

---

## SQL Developer

- SQL Developer 는 데이터베이스 연결, 워크시트, 테이블 GUI 생성 등 다양한 기능 존재
- 워크시트는 쿼리문을 입력하고 실행하는 텍스트 에디터로 볼 수 있다.
- 외부의 오라클도 접속해서 사용할 수 있다.

### 주요 기능

- 데이터베이스 개체 생성, 수정, 삭제 기능
- 다른 형식의 데이터 가져오기 및 내보내기 기능
- SQL*Plus 명령어 지원
- 다른 DBMS와 마이그레이션 지원
- SQL 문 자동 생성

---

## SQL*Plus

오라클의 가장 오래되고 기본적인 유틸리티

텍스트 기반으로 명령어가 처리된다.

### 몇 가지 사용법

```sql
-- 접속
sqlplus 사용자/비밀번호@DB이름 (또는 SID이름)

-- 접속 후 
HELP INDEX
HELP run

HELP SELECT -- SELECT는 sql*plus 명령이 아니라 일반 sql문 이므로 확인 불가하다.

sql*plus 전용 명령 뒤에는 세미콜론 안붙여도 된다.

DESCRIBE (DESC) 테이블 
-- 테이블의 구조를 보여준다.

LIST (L)
-- 마지막 수행된 SQL문을 보여준다.

RUN (/)
-- 마지막 SQL문을 다시 실행한다.

SHOW USER
-- 현재 사용자를 출력해 준다.

CONNECT HR/1234@XE
-- HR 사용자로 접속

COLUMN 열 이름 HEADING "출력이름" FORMAT 출력폭(A숫자)
-- 출력되는 열 이름을 변경하고 폭을 조절한다.

SAVE 경로 및 파일명
-- 화면에서 사용한 sql문이나 결과를 파일로 저장하거나 실행할 수 있다.

HOST
-- sql*plus를 종료하지 않고 잠깐 os로 빠져나간다.

EXIT
-- 다시 돌아온다.

START 경로 및 파일명.확장자 (@)
-- 파일을 실행

SPOOL 경로 및 파일명
-- sql*plus 화면 전체를 캡처해서 .lst 파일로 저장한다.

SET LINESIZE 숫자
SHOW LINESIZE
```

---

## 외부 오라클 서버 관리하기

Linux에서는 대부분 명령어 모드로만 사용하기 때문에 SQL Developer를 사용할 수 없다.

![image-20210610032845751](./img/2.png)

리눅스에 설치된 오라클에 외부 윈도우컴퓨터에서 접속하는 방법 : 161p

반대는 없나...

---

## 사용자 관리하기

SYSTEM 외의 별도의 사용자를 만들고 모든 권한이 아닌 적당한 권한을 부여해서 관리해야 한다.

- 권한 (Privileges) : SELECT 권한, INSERT 권한, CREATE 권한 등
- 역할 (Role) : 권한의 집합. (DBA 역할은 모든 권한이 포함되어 있음)

---