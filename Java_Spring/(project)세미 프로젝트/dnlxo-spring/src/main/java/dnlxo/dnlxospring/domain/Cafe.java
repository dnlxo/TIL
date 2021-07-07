package dnlxo.dnlxospring.domain;

public class Cafe { //상호명 대략위치, 대표메뉴, 가격, 주소, 이미지파일명, 하트 수, 상세정보 ur
    private String location;
    private String menu;
    private Long price;
    private String address;
    private String image;
    private Long heart;
    private String detail;

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public String getMenu() {
        return menu;
    }

    public void setMenu(String menu) {
        this.menu = menu;
    }

    public Long getPrice() {
        return price;
    }

    public void setPrice(Long price) {
        this.price = price;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }

    public Long getHeart() {
        return heart;
    }

    public void setHeart(Long heart) {
        this.heart = heart;
    }

    public String getDetail() {
        return detail;
    }

    public void setDetail(String detail) {
        this.detail = detail;
    }
}
