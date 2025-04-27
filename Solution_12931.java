public class Solution_12931 {

    public int solution(int n) {
        int answer = 0;
        int len = String.valueOf(n).length();
        while(len > 0){
            int 제수 = (int) Math.pow(10, len - 1);
            int 자리수 = n / 제수;
            answer += 자리수;
            n -= (제수 * 자리수);
            --len;
        }
        return answer;
    }
    public static void main(String[] args) {
        Solution_12931 instance = new Solution_12931();
        System.out.println(instance.solution(123));
    }
}
