import java.util.*;

public class cote2 {
    public static int searchIdx = 0;

    public static int minNum(int threshold, List<Integer> points) {
        if (threshold > points.get(points.size() - 1) - points.get(0)) {
            return points.size();
        }

        int searchNum = threshold + points.get(0); // 조건을 만족하는 최대 점수
        searchIdx = points.size() - 1; // 조건을 만족하려면 풀어야하는 최소 문제번호

        binarySearch(0, searchIdx, points, searchNum);
        searchIdx++;

        int answer = (searchIdx + 2) / 2;
        // 제일 적게 문제를 풀고싶기 때문에 무조건 1칸 띄엄띄엄 푼다.
        // 조건은 낚시 였던 것....
        return answer;
    }

    private static void binarySearch(int start, int end, List<Integer> points, int searchNum) {
        if (start <= end) {
            int mid = (start + end) / 2;
            int midNum = points.get(mid);

            if (midNum == searchNum) {
                searchIdx = mid;
                return;
            } else if (midNum >= searchNum) { // 조건 만족 왼쪽에서 탐색
                searchIdx = Math.min(searchIdx, mid); // 예를들어 조건이 최소 8점짜리 풀면되는데 
                //8점짜리 문제가 없고 7점이랑 9점짜리가 잇으면 9점짜리를 풀어야함
                binarySearch(start, mid - 1, points, searchNum);
            } else {
                binarySearch(mid + 1, end, points, searchNum);
            }
        }
    }

    // 1번
    public static String compressedString(String message) {
        String answer = "";
        char temp = message.charAt(0);
        int cnt = 1;

        for (int i = 1; i < message.length(); i++) {
            char m = message.charAt(i);

            if (m != temp) {
                answer += temp;
                if (cnt != 1) {
                    answer += ("" + cnt);
                }

                temp = m;
                cnt = 1;
            } else {
                cnt++;
            }
        }

        answer += temp;
        if (cnt != 1) {
            answer += ("" + cnt);
        }

        return answer;
    }

    public static int stockPairs(List<Integer> stocksProfit, long target) {
        int answer = 0;
        Set<Long> set = new HashSet<>();
        long num = stocksProfit.get(0);
        boolean same = false;
        set.add(num);

        for (int i = 1; i < stocksProfit.size(); i++) {
            long temp = stocksProfit.get(i);
            if (set.contains(temp)) {
                if (target == temp * 2) {
                    same = true;
                }
                continue;
            }

            if (set.contains(target - temp)) {
                answer++;
            }

            set.add(temp);
        }

        if (same) {
            answer++;
        }

        return answer;
    }
}
