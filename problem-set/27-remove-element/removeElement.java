import java.util.LinkedList;
import java.util.Queue;

class Solution {
public int removeElement(int[] nums, int val) {
        
        Queue<Integer> queue = new LinkedList<Integer>();

        int counter = 0;
        for(int i = 0; i < nums.length; i++){

            if(nums[i] == val){
                queue.add(i);
                counter++;
            }
            else if (!queue.isEmpty()){

                int index = queue.poll();
                nums[index] = nums[i];
                queue.add(i);
            }


        }
        return nums.length - counter;
    }
}