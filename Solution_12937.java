public class Solution_12937 {

    public String solution(int n) {
        return n % 2 == 0 ? "Even" : "Odd";
    }
    public static void main(String[] args) {
        Solution_12937 instance = new Solution_12937();
        System.out.println(instance.solution(1));
    }
}
