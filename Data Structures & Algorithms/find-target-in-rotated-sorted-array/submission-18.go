func search(nums []int, target int) int {
    for x:= 0; x < len(nums); x++ {
        if nums[x] == target {
            return x;
        }
    }
    return -1;
}
