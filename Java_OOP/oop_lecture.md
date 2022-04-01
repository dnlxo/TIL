- 객체의 핵싱은 기능 제공
- 객체는 기능으로 정의
- 메서드를 이용하여 기능 명세
  - 메서드 이름, 파라미터, 리턴값 으로 구성
- 객체와 객체는 메서드 호출을 이용하여 연결된다.

---

- 캡슐화란?
  - 데이터와 관련 기능을 묶는 것
  - **객체가 기능을 어떻게 구현했는지 외부에 감추는 것.**
  - 캡슐화는 정보 은닉의 의미를 포함한다.
  - **외부에 영향 없이 객체 내부 구현 변경이 가능하다.**
  - 캡슐화를 잘 하면 연쇄적인 코드 변경을 최소화 할 수 있다.
- 캡슐화를 위한 규칙
  - 데이터를 달라고 하지 말기(데이터를 가져와서 판단하지 말고), 해달라고 하기(직접 판단해줘라).
  - ex) if (account.getVersion() == Pro) {~~~} 가 아니고 if (account.hasProVersion()) {~} 이런 식으로
  - 데메테르의 법칙
    - 메서드에서 생성한 객체의 메서드만 호출해라 (메서드 하나를 호출하는 방식으로...)
    - 파라미터로 받은 객체의 메서드만 호출
    - 필드로 참조하는 객체의 메서드만 호출
      - ex) account.getExpiredDate().isAfter(now) >>> account.isExpired()

---

```java
public AuthResult authenticate(String id, String pw) {
  Member mem = findOne(id);
  if (mem == null) return AuthResult.NO_MATCH;
  
  if (mem.getVerificationEmailStatus() != 2) {
    return AuthResult.NO_EMAIL_VERIFIED;
  }
  if (passwordEncoder.isPasswordValid(mem.getPassword(), pw, mem.getId())) {
    return AuthResult.SUCCESS;
  }
  return AuthResult.NO_MATCH;
}

// 위 코드에서 캡슐화를 진행하면

public AuthResult authenticate(String id, String pw) {
  Member mem = findOne(id);
  if (mem == null) return AuthResult.NO_MATCH;
  
  if (!mem.isEmailVerified()) {
    return AuthResult.NO_EMAIL_VERIFIED;
  }
  if (passwordEncoder.isPasswordValid(mem.getPassword(), pw, mem.getId())) {
    return AuthResult.SUCCESS;
  }
  return AuthResult.NO_MATCH;
}
```

---

```java
public class Rental {
  private Movie movie;
  private int daysRented;
  
  public int getFrequentRenterPoints() {
    if (movie.getPriceCode() == Movie.NEW_RELEASE && daysRented > 1)
      return 2;
    else
      return 1;
  }
}

public class Movie {
  public static int REGULAR = 0;
  public static int NEW_RELEASE = 1;
  private int priceCode;
  
  public int getPriceCode() {
    return priceCode;
  }
}

// 위 코드에서 캡슐화를 진행하면

public class Rental {
  private Movie movie;
  private int daysRented;
  
  public int getFrequentRenterPoints() {
    return movie.getFrequentRenterPoints(daysRented);
  }
}

public class Movie {
  public static int REGULAR = 0;
  public static int NEW_RELEASE = 1;
  private int priceCode;
  
  public int getPriceCode() {
    return priceCode;
  }
  public int getFrequentRenterPoints(int daysRented) {
    if (priceCode == NEW_RELEASE && daysRented > 1)
      return 2;
    else
      return 1;
  }
}
```

---

```java
Timer t = new Timer();
t.startTime = System.currentTimeMillis();

t.stopTime = System.currentTimeMillis();

long elapsedTime = t.stopTime - t.startTime;

public class Timer {
  public long startTime;
  public long stopTime;
}

// 위 코드에서 캡슐화를 진행하면

Timer t = new Timer();
t.start();

t.stop();

long elapsedTime = t.elapsedTime(MILLISECOND);

public class Timer {
  public long startTime;
  public long stopTime;
  
  public void start() {
    this.startTime = System.currentTimeMillis();
  }
  
  public void stop() {
    this.stopTime = System.currentTimeMillis();
  }
  
  public long elapsedTime(TimeUnit unit) {
    switch(unit) {
      case MILLISECOND :
        return stopTime - startTime;
    }
  }
}
```

---

```java
public void verifyEmail(String token) {
  Member mem = findByToken(token);
  if (mem == null) throw new BadTokenException();
  
  if (mem.getVerificationEmailStatus() == 2) {
    throw new AlreadyVerifiedException();
  } else {
    mem.setVerificationEmailStatus(2);
  }
}

// 위 코드에서 캡슐화를 진행하면

public void verifyEmail(String token) {
  Member mem = findByToken(token);
  if (mem == null) throw new BadTokenException();
  
  mem.verifyEmail();
}

public class Member {
  private int verificationEmailStatus;
  
  public void verifyEmail() {
    if (isEmailVerified())
      throw new AlreadyVerifiedException();
    else
      this.VerificationEmailStatus = 2;
  }
  
  public boolean isEmailVerified() {
    return verificationEmailStatus == 2;
  }
  
```

---

- 추상화
  - 객체지향적 프로그래밍을 하는데 필수적 요소
  - 데이터나 프로세스 등을 의미가 비슷한 개념, 혹은 의미있는 표현으로 정의하는 과정
  - 특정한 성질, 공통 성질을 뽑아내는 방식으로 추상화를 진행한다.
    - Money 클래스 : 통화, 금액
    - USER 클래스 : 아이디, 이름, 이메일
- 다형성 (Polymorphism)
  - 여러 모습을 갖는 것
  - 한 객체가 여러 타입의 기능을 제공하는 것
  - 타입 상속을 통해 다형성을 구현
- 타입 추상화
  - 여러 구현 클래스를 대표하는 상위 타입을 도출해내기
  - 보통 인터페이스로 추상화
  - ex) EmailNotifier, SMSNotifier, KakaoNotifier 클래스들이 있을 때, Notifier 라는 인터페이스로 추상화.
  - 기능의 구현이 아닌 의도를 더 잘 드러낸다.

---

- 상속과 재사용
- 상위 클래스의 기능을 재사용, 확장할 수 있다는 이점이 있으나....
- 이러면 상위 클래스를 변경하기 어려워진다.
  - 여러 하위 클래스에 계층적으로 모두 영향을 미침
- 클래스가 너무 많아지기도 하고, 상속하면서 메소드 오용이 생길 수 있다.
- 상속의 단점을 해결하기 위해서는 조립을 이용한다.
- 여러 객체를 묶어서 더 복잡한 기능을 제공하면 된다.
- 클래스 안에 새로운 객체를 생성하고 재사용하면 된다.

---

- 기능과 책임 분리
- 하나의 기능은 여러 하위 기능으로 분리가 가능하다.
- 기능을 알맞은 객체에게 부여해야한다.

---

- 의존과 DI
- 의존이란?
  - 기능 구현을 위해 다른 구성요소를 사용하는 것
  - ex) 객체 생성, 메서드 호출, 데이터 사용
  - 따라서 의존은 변경이 전파될 가능성이 있다.
  - 순환 의존이 발생하지 않도록 해야한다.
  - 의존하는 대상은 적을수록 좋다.
    - 한 클래스에 기능이 많은 경우... 위험하니까 기능 별로 클래스를 분류하는 것을 고려해라
    - 의존 대상이 많을 때 의존 대상 여러개(비슷한 기능을 하는..) 를 하나로 묶어볼 수 있나 고려
  - 의존 대상 객체를 직접 생성하지 않는 방법으로는 DI가 있다.
    - 외부에서 의존 객체를 주입하는 방법
    - 즉, 생성자나 메서드를 이용해서 주입한다.
    - 객체를 내부에서 생성할 것이냐 외부에서 생성해서 전달받을 것이냐의 차이다.
    - 객체를 내부에서 생성하면 생성한 객체가 바뀌었을때 같이 수정해야할 가능성이 매우 높다. 이것을 강결합이라고 부른다.
    - 객체를 외부에서 주입받게 되면 그 객체와의 의존도가 낮아진다. 객체가 수정되었을때도 영향을 덜 받는다. 약결합이라 부른다.
    - 스프링에서는 다양한 객체들을 스프링 컨테이너에 미리 담아두기 때문에 원하는 객체를 주입받아 사용하기 편하다.

---

