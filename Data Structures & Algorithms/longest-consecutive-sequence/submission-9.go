func longestConsecutive(nums []int) int {
    if len(nums) <= 1 { return len(nums)}
    sort.Ints(nums)
    count := 1
    max := 0
    for idx := 1; idx<len(nums); idx++ {
        if nums[idx-1] == nums[idx]-1 {
            count += 1
        }else if nums[idx-1] == nums[idx] {
        } else {
            count = 1
        }
        if max < count {
                max = count
            }
    }
    return max
}
