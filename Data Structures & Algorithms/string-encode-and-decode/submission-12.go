type Solution struct{}

// if strs == []: return "😉None"
//         if strs == [""]: return ""
//         return "😉".join(strs)
func (s *Solution) Encode(strs []string) string {
    buf := ""

    if len(strs) == 0 {
        return "😉None"
    }

    for idx, v := range strs {
        buf = buf + string(v)
        if idx < len(strs) -1 {
            buf = buf + string("😉")
        }
    }
    if len(buf) == 0{
        return ""
    }
    
    return buf
}

func (s *Solution) Decode(encoded string) []string {
    if encoded == "😉None"{ return []string{} }
    parts := strings.Split(encoded, "😉")
    return parts
}
