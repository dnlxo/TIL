import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.Set;
import java.util.EmptyStackException;

public class Test {

    public static String compressedString(String message) {
        String answer = "";
        char temp = message.charAt(0);
        int cnt = 1;

        for (int i = 1; i < message.length(); i++) {
            if (temp == message.charAt(i)) {
                cnt++;
            } else {
                answer += temp;
                if (cnt != 1) {
                    answer += ("" + cnt);
                }
                temp = message.charAt(i);
                cnt = 1;
            }
        }
        // aaaabbbcdd
        // 한바퀴만 돈다. O(n)에 해결 가능하도록.
        // 전에 어떤 문자였는지 알고 있어야하며, 그 문자가 몇번 연속해서 나오고있는지 알아야함
        // temp = message.charAt(0) , cnt = 1
        answer += temp;
        if (cnt != 1) {
            answer += ("" + cnt);
        }
        return answer;
    }

    //멀티스레드 환경에서는 스트링 버퍼를 쓰는걸로..

    public static int stockPairs(List<Integer> stocksProfit, long target) {
        // (3,3,9,9,6,6,5,7,3) 이렇게 있고, target 12 면 3,9 6,6 5,7 이렇게 세쌍 그래서 답은 3 이렇게 나와야합니다.
        // twosum이랑 유사한데, 3,9 == 9,3 == 3,9 같은걸로 쳐야한다는... 그래서 이걸먼저 해결위해서
        // 한번 들어간애는 걍 아무것도안하고 넘어갑니다.
        // hashset을 이용한 이유는. 일단 키:밸류 로 탐색이 O(1)이거든요 그래서 전체 주식 목록[ 리스트 ]이걸 한바퀴만 돌고 문제를
        // 풀수있습니다. O(N)으로 풀수가있습니다.

        // 풀이 방식은 (3) 9를 넣기전에 더해서 12가 되도록하는애가 잇나?/ 있으면 answer++ 하면됩니다.
        int answer = 0;
        Set<Long> set = new HashSet<>();
        long num = stocksProfit.get(0);
        set.add(num);
        boolean flag = false;

        for (int i = 1; i < stocksProfit.size(); i++) {
            long temp = stocksProfit.get(i);
            if (set.contains(temp)) {
                if (temp * 2 == target) {
                    flag = true;
                }
                continue;
            }

            if (set.contains(target - temp)) {
                answer++;
                set.add(temp);
            }
        }
        if (flag) {
            answer++;
        }
        return answer;
    }

    //키값에 해시함수를 적용해서 인덱스 번호로 바꿉니다. 그리고 그 인덱스를 따라가보면 실제 밸류값이 있도록..
    // 근데 키값에 해시함수를 돌렷는데 키값이 다른데도 인덱스번호가 같은겨우가잇어요... 그러면이제 
    // 그 위치에 노드를 하나더 연결해서 (리스트면 append한다고 할수도..)저장을 합니다.
    // 그래서 중복 인덱스번호가 많음녀 O(1)은 아닌거죠


    //5번문제 ㄲ지만 풀면된다? 그러면 0번 2번 4번 5번 이렇게 푸렴ㄴ되거든요??? 5+2 +1 / 2 = 4
    // 6번문제                  0번 2번 4번 6번           6+2 +1 / 2 == 4
    // 7점 9점 짜리만 잇으면 타겟은 8인데........ 9를 풀어야된단말이에요.. 
    // 근데 재귀쓰다보니까 전역변수를 놔주는게 편하잖아요? 그래서 하나 놨씁니다.

    public static int searchIdx = 0;

    public static int minNum(int threshold, List<Integer> points) {
        if (threshold > points.get(points.size() - 1) - points.get(0)) {
            return points.size();
        }

        int searchNum = threshold + points.get(0);
        searchIdx = points.size() - 1;

        binarySearch(0, searchIdx, points, searchNum);
        searchIdx++;

        int answer = (searchIdx + 2) / 2;
        return answer;
    }

    private static void binarySearch(int start, int end, List<Integer> points, int searchNum) {
        if (start <= end) { //재귀 탈출조건
            int mid = (start + end) / 2;
            int midNum = points.get(mid);
    
            // 왼쪽에서 재귀
            if (searchNum == midNum) {
                searchIdx = mid;
                return;
            }
            else if (searchNum <= midNum) {
                searchIdx = Math.min(searchIdx, mid);
                binarySearch(start, mid - 1, points, searchNum);
            } else {
                binarySearch(mid + 1, end, points, searchNum);
            }
            
        }
    }


    public static void bubble(int[] arr) {
        int temp = 0;
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length - i; j++) {
                if (arr[j-1] > arr[j]) {
                    temp = arr[j-1];
                    arr[j-1] = arr[j];
                    arr[j] = temp;
                }
            }
        }
    }

    public static void select(int[] arr){
        int temp = 0;
        int minIdx = 0;
        // 루트가 두번들어가는데 두번쨰 루프는 한칸뒤에서 실행...
        for (int i = 0; i < arr.length; i++) {
            minIdx = i;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[j] < arr[minIdx]) {
                    minIdx = j;
                }
            }
            temp = arr[i];
            arr[i] = arr[minIdx];
            arr[minIdx] = temp;
        }
        System.out.println(Arrays.toString(arr));
    }

    public static void quick(int[] arr, int left, int right) {
        if (left >= right) {
            return ; //재귀 탈출조건
        }
        // 피봇 설정 후 정렬
        int pivotIdx = partition(arr, left, right);
        //왼쪽에서 퀵 진행
        quick(arr, left, pivotIdx - 1);
        //오른쪽에서 퀵 진행
        quick(arr, pivotIdx + 1, right);
    }
// 1,2,3,5,7,6,8
    public static int partition(int[] arr, int left, int right) {
        int pivot = arr[(left + right) / 2];

        while (left < right) {
            while (arr[left] < pivot) {
                left++;
            }
            while (arr[right] > pivot) {
                right--;
            }
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
        }
        return left;
    }    

    public static void main(String[] args) {
        System.out.println(compressedString("aaaabbbcdd"));
        int[] arr = {8,7,5,3,6,2,1};
        quick(arr, 0, arr.length - 1);
        System.out.println(Arrays.toString(arr));
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
        }
        List<Integer> a = new ArrayList<>();
        a.add(5);
        System.out.println(a.toString());
        MyQueue<Integer> q = new MyQueue<>();

    }
}

class MyStack<T> {
    class Node<T> {
        private T data;
        private Node<T> next;
        
        public Node(T data) {
            this.data = data;
        }
    }

    private Node<T> top;

    public void push(T item) {
        Node<T> node = new Node<T>(item);
        node.next = top;
        top = node;
    }

    public T pop() {
        if (top == null) {
            throw new EmptyStackException();
        }
        T item = top.data;
        top = top.next;
        return item;
    }
}

class MyQueue<T> {
    class Node<T> {
        private T data;
        private Node<T> next;
        
        public Node(T data) {
            this.data = data;
        }
    }

    private Node<T> left;
    private Node<T> right;

    public void append(T item) {
        Node<T> node = new Node<T>(item);

        if (right != null) {
            right.next = node;
        }
        right = node;
        if (left == null) {
            left = node;
        }
    }

    public T popleft() {
        if (left == null) {
            throw new NoSuchElementException();
        }
        T item = left.data;
        left = left.next;
        if (left == null) {
            right = null;
        }
        return item;
    }

    public boolean isEmpty() {
        if (left == null) {
            return true;
        } else return false;
    }
}