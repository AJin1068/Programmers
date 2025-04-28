public class Solution_12918 {

    public boolean solution(String s) {
        int len = s.length();
        if(len != 4 && len != 6) return false;
        for(int i = 0; i <len; i++){
            int a = (int) s.charAt(i);
            if(a < 48 || a > 57) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        String s = "123a214T009934365";
        Solution_12918 instance = new Solution_12918();
        System.out.println(instance.solution(s));
    }
}
