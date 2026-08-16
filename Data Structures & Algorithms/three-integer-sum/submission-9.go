// import "slices"


func threeSum(nums []int) [][]int {
    if len(nums) < 3 {
        return [][]int{}
    }
    sort.Ints(nums)
    fmt.Println(nums)
    result := [][]int{}
    set := map[int]struct{}{}
    for tdx := 2; tdx < len(nums); tdx++ {
        cur := -nums[tdx]
        izq, der := 0, tdx-1
        for izq < der {
            par := nums[der] + nums[izq]
            if cur == par {
                item := []int{nums[izq], nums[der], -par}
                hash:= (((nums[izq]*31)+nums[der])*31)+par
                _, v := set[hash]
                if !v {
                    result = append(result, item)
                    set[hash] = struct{}{}
                }
                izq++
            } else if cur >= par {
                izq++
            } else if cur < par {
                der--
            }
        }
    }
    return result
}
