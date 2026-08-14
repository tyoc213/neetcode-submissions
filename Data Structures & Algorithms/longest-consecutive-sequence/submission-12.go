func longestConsecutive(nums []int) int {
    if len(nums) <= 1 { return len(nums)}
    sort.Ints(nums)
    count := 1
    maxint := 0
    for idx := 1; idx<len(nums); idx++ {
        diff := nums[idx]-nums[idx-1]
        if diff > 1 {
            count = 1
        } else {
            count += diff
        }
        if maxint < count {
            maxint = count
        }
    }
    return maxint
}
