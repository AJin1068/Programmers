import java.util.*;

public class Solution_1845 {

    public int solution(int[] nums) {
        int max = nums.length/2;
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        return max < set.size() ? max : set.size();
    }
    public static void main(String[] args) {
        Solution_1845 instance = new Solution_1845();
        int[] nums = {3, 1, 2, 3};
        System.out.println(instance.solution(nums));
    }
}
