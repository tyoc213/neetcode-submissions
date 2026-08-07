class Solution {
    public boolean hasDuplicate(int[] nums) {
        Hashtable<Integer,Integer> hs= new Hashtable<>();
		for (int i=0; i<nums.length; i++) {
			if (hs.containsKey(nums[i]) == false) {
				hs.put(nums[i], 0);
			} else {
				return true;
			}
			
		}
		return false;
    }
}