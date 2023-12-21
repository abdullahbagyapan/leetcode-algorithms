class Solution {
    public int maxArea(int[] height) {
        
        int maxArea = 0;
        int leftPointer = 0;
        int rightPointer = height.length - 1;

        while (leftPointer < rightPointer) {

            int leftLine = height[leftPointer];
            int rightLine = height[rightPointer];

            int distance = rightPointer - leftPointer;
            int maxHeight = Math.min(leftLine, rightLine);
            
            int area = maxHeight * distance;
            
            maxArea = Math.max(area, maxArea);
            
            if (leftLine < rightLine) {
                leftPointer++;
            }
            else {
                rightPointer--;
            }
        }

        return maxArea;
    }
}