package com.example.apiexample.controller;

import com.example.apiexample.model.UserProfile;
import org.springframework.web.bind.annotation.*;

import javax.annotation.PostConstruct;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
public class UserProfileController {

    private Map<String, UserProfile> userMap;

    @PostConstruct //
    public void init() {
        userMap = new HashMap<String, UserProfile>();
        userMap.put("1", new UserProfile("1", "홍길동", "111-1111", "서울시 강남구 대치1동"));
        userMap.put("2", new UserProfile("2", "홍길자", "111-1111", "서울시 강남구 대치2동"));
        userMap.put("3", new UserProfile("3", "홍길순", "111-1111", "서울시 강남구 대치3동"));
    }

    @GetMapping("/user/{id}")
    public UserProfile getUserProfile(@PathVariable("id") String id) {
        return userMap.get(id);
    }

    @PostMapping("/user/all")
    public List<UserProfile> getUserProfileList() {
        return new ArrayList<UserProfile>(userMap.values());
    }

    @PostMapping("/user/{id}")
    public void insertUserProfile(@PathVariable("id") String id, @RequestParam("name") String name, @RequestParam("phone") String phone,
                                  @RequestParam("address") String address) {
        userMap.put(id, new UserProfile(id, name, phone, address));
    }

    @PutMapping("/user/{id}")
    public void putUserProfile(@PathVariable("id") String id, @RequestParam("name") String name, @RequestParam("phone") String phone,
                               @RequestParam("address") String address) {
        UserProfile userProfile = userMap.get(id);
        userProfile.setName(name);
        userProfile.setPhone(phone);
        userProfile.setAddress(address);
    }
}
