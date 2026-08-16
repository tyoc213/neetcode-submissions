func maxArea(heights []int) int {
	izq, der := 0, len(heights)-1
	total := -1
	for izq < der && izq < len(heights)-1 {
		area := (der-izq)*min(heights[izq], heights[der])
		total = max(total, area)
		if heights[izq] < heights[der] {
			izq++
		} else {
			der--
		}
	}
	return total
}
