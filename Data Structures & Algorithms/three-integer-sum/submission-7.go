import "slices"
func ContainsSlice(outer [][]int, inner []int) bool {
	return slices.ContainsFunc(outer, func(sub []int) bool {
		if len(sub) != len(inner) {
			return false
		}
		for i, v := range inner {
			if sub[i] != v {
				return false
			}
		}
		return true
	})
}

func threeSum(nums []int) [][]int {
    if len(nums) < 3 {
        return [][]int{}
    }
    sort.Ints(nums)
    fmt.Println(nums)
    result := [][]int{}
    for tdx := 2; tdx < len(nums); tdx++ {
        cur := -nums[tdx]
        izq, der := 0, tdx-1
        for izq < der {
            par := nums[der] + nums[izq]
            if cur == par {
                item := []int{nums[izq], nums[der], -par}
                if !ContainsSlice(result, item) {
                    result = append(result, item)
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
