class Solution {
    public boolean hasDuplicate(int[] nums) {
        Hashtable hs = new Hashtable();
		for (int i=0; i<nums.length; i++) {
			if (hs.containsKey(nums[i])) {
				return true;
			}
			hs.put(nums[i], 0);
		}
		return false;
    }
}