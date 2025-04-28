import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Solution_42576 {

    public String solution(String[] participant, String[] completion) {
        String answer = "";
        List<String> participantList =  new ArrayList<>(List.of(participant));
        List<String> completionList =  new ArrayList<>(List.of(completion));
        Collections.sort(participantList);
        Collections.sort(completionList);
        for(int i = 0; i < participantList.size(); i++) {
            if(!participantList.get(i).equals(completionList.get(i)) || i == participantList.size() - 1) {
                answer = participantList.get(i);
                break;
            }
        }
        return answer;
    }
    public static void main(String[] args) {
        Solution_42576 instance = new Solution_42576();
        String[] participant = {"mislav", "stanko", "mislav", "ana"};
        String[] completion = {"stanko", "ana", "mislav"};
        System.out.println(instance.solution(participant, completion));
    }
}
