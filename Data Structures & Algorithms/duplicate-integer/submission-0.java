class Solution {
    public boolean hasDuplicate(int[] nums) {

        //sorted the array
        java.util.Arrays.sort(nums);
        for (int x = 0; x < nums.length - 1; x++){
            if (nums[x] == nums[x+1]){
                return true;
            }
        }

        return false;
    }
}