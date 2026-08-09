func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	var freq [26]int
    var negatives int
	
	for i := range s {
        if freq[s[i]-'a'] == -1 {
            negatives -= 1
        }
		freq[s[i]-'a']++
		freq[t[i]-'a']--
        if freq[t[i]-'a'] == -1 {
            negatives += 1
        }
	}

	for _, v := range freq {
		if v != 0 {
			return false
		}
	}

	return true
}