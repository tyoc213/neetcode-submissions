func groupAnagrams(strs []string) [][]string {
	result := [][]string{};
	hashmap := make(map[uint64][]string);
	for _, s := range strs {
		counts := [26]int{}
		for icx, c := range(s) {
			print(icx, c)
			counts[c-'a'] += 1
		}

		var hash uint64
		for _, x := range counts {
			hash ^= uint64(x)
			hash *= 16777619 // FNV prime
		}
		hashmap[hash] = append(hashmap[hash], s)
	}
	for _, v := range hashmap {
		result = append(result, v)
	}

	return result;
}
