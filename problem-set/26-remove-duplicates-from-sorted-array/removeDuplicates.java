import java.util.*;

class Solution {
    public int removeDuplicates(int[] nums) {
        LinkedHashSet<Integer> linkedHashSet = new LinkedHashSet<>();
    
        for (Integer num:nums) {
            linkedHashSet.add(num);
        }
        Iterator<Integer> iterator = linkedHashSet.iterator();

        int i = 0;
        while (iterator.hasNext()) {
            nums[i] = iterator.next();
            i++;
        }

        return i++;
    }
}