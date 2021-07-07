package dnlxo.dnlxospring.controller;

public class MemberForm {
    private String name;
    private String pw;
    private String id;
    private String pwCheck;

    public String getPwCheck() {
        return pwCheck;
    }

    public void setPwCheck(String pwCheck) {
        this.pwCheck = pwCheck;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getPw() {
        return pw;
    }

    public void setPw(String pw) {
        this.pw = pw;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
}
