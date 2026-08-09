
func twoSum(nums []int, target int) []int {
	h := map[int]int{}
	for i := 0; i<len(nums); i++ {
		diff := target - nums[i];
		_,e := h[diff];
		if e {
			v := []int{i, h[diff]};
			sort.Ints(v);
			return v;
		}
		h[nums[i]] = i;
	}
	return []int{};
}
