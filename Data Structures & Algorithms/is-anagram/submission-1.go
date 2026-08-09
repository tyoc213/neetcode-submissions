import "maps"

func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
            return false;
        }
        ms := map[byte]int{}
        mt := map[byte]int{}
        for i := 0; i<len(s); i++ {
            ms[s[i]] += 1
            mt[t[i]] += 1
        }
        return maps.Equal(ms, mt)
}
