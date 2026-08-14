func isASCIIAlpha(r byte) bool {
    return (r >= 'A' && r <= 'Z') || (r >= 'a' && r <= 'z') || (r >= '0' && r <= '9')
}

func equalIgnoreCase(a, b byte) bool {
    if a >= 'a' && a <= 'z' {
        a -= 'a' - 'A'
    }

    if b >= 'a' && b <= 'z' {
        b -= 'a' - 'A'
    }

    return a == b
}



func isPalindrome(s string) bool {
    izq, der := 0, len(s)-1

    for izq < der {
        if !isASCIIAlpha(s[izq]){
            izq++
            continue
        } else if !isASCIIAlpha(s[der]){
            der--
            continue
        }
        if !equalIgnoreCase(s[izq], s[der]) {
            return false
        }
        izq ++
        der --
    }
    return true
}
