class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        HashMap<Integer, Integer> map = new HashMap<>();
        int [] results = new int[2];
        for(int i = 0; i < nums.length; i++){
            int get_val = map.getOrDefault(target-nums[i], -1);
            if(get_val != -1){
                results[0] = map.get(target-nums[i]);
                results[1] = i;
                return results;
            } else{
                map.put(nums[i], i);
            }
        }
        return results;
    }
}
