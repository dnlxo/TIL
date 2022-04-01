import java.util.*;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}
public class Cote {
    // backtracking recursion termination check
    List<String> ret = new ArrayList<>();

    // 트리 순회 (재귀)
    // preorder : self left right
    // inorder : left self right
    // postorder : left right self
    // 이진 검색 트리 ? 자기 왼쪽은 자기보다 작고,, 오른쪽은 자기보다 큼.. 
    // 따라서 inorder 순회를 하면 오름차순 정렬이 된다.
    public void inorder(TreeNode root) {
        if (root == null) return;
        inorder(root.left);
        // self 처리
        inorder(root.right);
    }
    static int[] dp = new int[10000];

    public static int sol(int n) {
        if (n == 0) { return 0; }
        if (n == 1) { return 1; }
        if (n == 2) { return 2; }
        if (dp[n] != 0) { return dp[n]; }
        dp[n] = sol(n-1) + sol(n-2);
        return dp[n];
    }
    // walker runner technic
    // walker 한번에 한칸, runner 한번에 두칸
    // runner 골인? walker 중간
    // 1 2 3 4 5 6 7 8
    // 1 2 3 4 5 6 7 8
    // 즉 러너 1칸 워커 1칸 러너 1칸 반복
    public ListNode middleNode(ListNode head) {
        ListNode walker = head;
        ListNode runner = head;
        while(runner != null) {
            runner = runner.next;
            if (runner != null) {
                walker = walker.next;
                runner = runner.next;
            }
        }
        return walker;
    }

    // Two Sum
    // nums = [2, 7, 11, 15], target = 9
    // 음 일단 배열을 두번 루프 돌면 무조건 해를 찾을 수 있다.
    // 루프를 1개 돌면서 
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int cur = nums[i];
            if (map.containsKey(target - cur)) {
                int[] ret = new int[2];
                ret[0] = map.get(target - cur);
                ret[1] = i;
                return ret;
            } else {
                map.put(cur, i);
            }
        }
        return null;
    }

    public static List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> ret = new ArrayList<>();
        if (root == null) return ret;
        
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);

        while (!q.isEmpty()) {
            List<Integer> level = new ArrayList<>();
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = q.poll();
                level.add(node.val);
                if (node.left != null) q.offer(node.left);
                if (node.right != null) q.offer(node.right);
            }
            ret.add(0, level);
        }
        return ret;
    }


    public static void main(String[] args) {
        String s = "{[]()}";
        Stack<Character> st = new Stack<>();
        char[] arr = s.toCharArray();
        for (char c : arr) {
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            } else if (c == ')') {
                if(st.size() == 0 || st.pop() != '(') {
                    System.out.println("false");
                }
            }
        }
        
        System.out.println(sol(5));

        TreeNode node1 = new TreeNode(3);
        TreeNode node2 = new TreeNode(9);
        TreeNode node3 = new TreeNode(20);
        TreeNode node4 = new TreeNode(15);
        TreeNode node5 = new TreeNode(7);
        node1.left = node2;
        node1.right = node3;
        node3.left = node4;
        node3.right = node5;

        List<List<Integer>> soln = levelOrderBottom(node1);
        System.out.println(soln);
    }
}
