import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;

public class HashMap1 {
    
    public static void main(String[] args) {
        HashMap<String, Integer> a = new HashMap<String, Integer>();
        a.put("one", 1);
        a.put("two", 2);

        // entrySet 이용방법
        for (Map.Entry<String, Integer> entry : a.entrySet()) {
            System.out.println(entry.getKey() + " : " + entry.getValue());
        }

        System.out.println("------------");

        // keySet 이용방법
        for (String key : a.keySet()) {
            System.out.println(key + " : " + a.get(key));
        }

        System.out.println("lambda stream------------");

        // lambda 이용방법
        a.entrySet().stream().forEach(entry -> {
            System.out.println(entry.getKey() + " : " + entry.getValue());
        });
        a.keySet().stream().forEach(key -> {
            System.out.println(key + " : " + a.get(key));
        });

        System.out.println("오름차순------------");

        // 오름차순
        a.entrySet().stream().sorted(Map.Entry.comparingByKey(Comparator.reverseOrder())).forEach(entry -> {
            System.out.println(entry.getKey() + " : " + entry.getValue());
        });
    }
}
