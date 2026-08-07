func hasDuplicate(nums []int) bool {
	s := map[int]struct{}{}
    for x:=0; x<len(nums); x++ {
		_, existe := s[nums[x]]
		if existe {
			return true
		}
		s[nums[x]] = struct{}{}
	}
	return false
}
